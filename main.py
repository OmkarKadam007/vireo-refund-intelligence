import streamlit as st
import pandas as pd
import numpy as np
import re
from pathlib import Path
import plotly.express as px

st.set_page_config(page_title="Vireo Refund Intelligence", layout="wide")

# Set up paths
BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

@st.cache_data
def load_and_process_data():
    # 1. Load Data
    tickets = pd.read_csv(RAW_DATA_DIR / "tickets.csv")
    agents = pd.read_csv(RAW_DATA_DIR / "agents.csv")
    
    # 2. Fix the 1 Crore Bug (Clean Data)
    tickets['refund_amount_inr'] = pd.to_numeric(tickets['refund_amount_inr'], errors='coerce').fillna(0)
    mask_legacy = tickets['source_system'] == 'legacy_fd'
    tickets.loc[mask_legacy, 'refund_amount_inr'] = tickets.loc[mask_legacy, 'refund_amount_inr'] / 100
    
    tickets = tickets.sort_values(by=['ticket_id', 'source_system'])
    tickets = tickets.drop_duplicates(subset=['ticket_id'], keep='first')
    
    # Merge with agents
    merged = tickets.merge(
        agents[['agent_id', 'name', 'team']].drop_duplicates(subset=['agent_id']), 
        on='agent_id', how='left'
    )
    
    # 3. NLP Rule Engine for GW-OTHER
    def smart_classify(row):
        text = str(row['customer_message']).lower() + " " + str(row['agent_notes']).lower()
        if re.search(r'\b(doa|dead|not working|broken|defective|right out of the box)\b', text): return 'DOA-REPL'
        if re.search(r'\b(lost|not delivered|transit|tracking|missing)\b', text): return 'LOST-TRANSIT'
        if re.search(r'\b(duplicate|charged twice|double)\b', text): return 'DUP-PAYMENT'
        if re.search(r'\b(cancel|changed mind|mistake)\b', text): return 'CANCEL'
        if re.search(r'\b(price|coupon|discount|cheaper)\b', text): return 'PRICE-ADJ'
        if re.search(r'\b(warranty|buyback)\b', text): return 'WTY-BUYBACK'
        if re.search(r'\b(return|qc|quality)\b', text): return 'RETURN-QC-OK'
        return 'GW-OTHER'
    
    merged['corrected_reason_code'] = merged['refund_reason_code']
    mask = (merged['refund_reason_code'] == 'GW-OTHER') & (merged['refund_amount_inr'] > 0)
    merged.loc[mask, 'corrected_reason_code'] = merged[mask].apply(smart_classify, axis=1)
    
    return merged

# UI Layout
st.title("Vireo Audio - Refund Intelligence")
st.markdown("Automated reconciliation of the Q3 Finance variance and NLP-based correction of frontline agent misclassification.")

try:
    df = load_and_process_data()
    
    # Top Metrics
    col1, col2, col3 = st.columns(3)
    total_refunds = df['refund_amount_inr'].sum()
    original_gw = df[(df['refund_reason_code'] == 'GW-OTHER') & (df['refund_amount_inr'] > 0)]['refund_amount_inr'].sum()
    new_gw = df[(df['corrected_reason_code'] == 'GW-OTHER') & (df['refund_amount_inr'] > 0)]['refund_amount_inr'].sum()
    
    col1.metric("Verified 18-Mo Total Refunds", f"₹ {total_refunds:,.0f}", "Fixes 1 Cr Finance Bug", delta_color="inverse")
    col2.metric("Original GW-OTHER Exposure", f"₹ {original_gw:,.0f}")
    col3.metric("Corrected GW-OTHER Exposure", f"₹ {new_gw:,.0f}", f"-₹ {original_gw - new_gw:,.0f} recovered", delta_color="normal")
    
    st.divider()
    
    # Visualizations
    st.subheader("Refund Distribution: Reported vs. Actual (NLP Corrected)")
    
    before_dist = df[df['refund_amount_inr'] > 0].groupby('refund_reason_code')['refund_amount_inr'].sum().reset_index()
    after_dist = df[df['refund_amount_inr'] > 0].groupby('corrected_reason_code')['refund_amount_inr'].sum().reset_index()
    
    colA, colB = st.columns(2)
    with colA:
        fig1 = px.pie(before_dist, values='refund_amount_inr', names='refund_reason_code', title="Original Agent Input (Heavy GW-OTHER Bias)")
        st.plotly_chart(fig1, use_container_width=True)
    with colB:
        fig2 = px.pie(after_dist, values='refund_amount_inr', names='corrected_reason_code', title="NLP Corrected Distribution")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("High-Risk Agents (Most remaining GW-OTHER usage)")
    risk_agents = df[(df['corrected_reason_code'] == 'GW-OTHER') & (df['refund_amount_inr'] > 0)]
    risk_summary = risk_agents.groupby(['name', 'team'])['refund_amount_inr'].sum().reset_index().sort_values('refund_amount_inr', ascending=False).head(5)
    st.dataframe(risk_summary, use_container_width=True)

except Exception as e:
    st.error(f"Failed to load data. Ensure CSV files are in data/raw/. Error: {e}")