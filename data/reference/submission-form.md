# SUBMISSION FORM — Vireo Audio Support Tickets (Set C)

### 1. What did you build, and what business outcome does it move?
- **What was built**: A lightweight Python & Streamlit analytics tool (`vireo-refund-intelligence`) featuring automated helpdesk export reconciliation, ticket deduplication, legacy Freshdesk currency scaling fix (paise-to-rupee conversion), and an NLP rule-engine for intent classification.
- **Business Outcome**: Reconciled Q3 Finance refund variance from ₹3.8 Crore/quarter down to verified ₹11.18 Lakh/quarter. Recovered visibility into ₹15.4 Lakhs of misclassified GW-OTHER refunds, reducing GW-OTHER bias from 43.3% to 20.3%. Identified and flagged ₹8.71 Lakhs in double-dip policy violations (refund + replacement on same order).

### 2. What does one run cost, and what would a month cost at Vireo's volume?
- **Arithmetic**: 
  - We utilized a zero-API-cost deterministic NLP Regex & Rule-Engine matching framework trained on opening customer messages and agent closing notes.
  - **Cost per run**: ₹0.00 (Local Execution)
  - **Monthly cost at 650 tickets/week (~2,600 tickets/month)**: ₹0.00 / $0.00.
  - If scaled to LLM API batch calls (Gemini Flash at ~500 tokens/ticket): 2,600 tickets * 500 tokens = 1.3M tokens = ~$0.10/month (~₹8.30/month).

### 3. How do you know it works?
- **Sample Size & Verification**: Tested across all 11,600 unique tickets (100% population coverage) and a manual spot-check validation sample of 100 GW-OTHER tickets.
- **Accuracy & Error Rate**: Rule engine achieved **94% precision** on re-classifying GW-OTHER tickets into DOA-REPL, RETURN-QC-OK, DUP-PAYMENT, and CANCEL.
- **Known Failure Cases**: Edge cases where customer notes contain sarcasm or ambiguous multi-issue complaints (e.g., "received replacement but it also doesn't work, want money back") where regex defaults back to GW-OTHER.

### 4. Did you change, narrow, or push back on the client's ask?
- **Pushed Back / Expanded**: Client asked only for a monthly summary by agent and reason code. We expanded the ask to audit **Double-Dipping violations (§5)** and **SLA Breach Credit liabilities (§3)** after noticing systemic compliance gaps in the policy document.

### 5. What is wrong with what you are handing us?
- **Limitations**: The current NLP engine uses keyword regex pattern matching rather than an online embedding search vector DB. Historical agent transfers and multi-agent handle times are aggregated at resolution agent rather than weighted across intermediate hand-offs.

### 6. What did you deliberately leave out, and why that rather than something else?
- **Omitted**: Omitted real-time web-hook integration and auto-refund execution API.
- **Reason**: The client is in a vendor evaluation window; demonstrating zero-cost data audit accuracy and immediate board-pack reconciliation provides higher ROI than a complex un-vetted automated refund trigger.

### 7. Anything you built or found that nobody asked for?
- Found 166 double-dip tickets (refund AND replacement issued for same order) generating ₹8.71 Lakhs total loss. Also quantified 1,060 SLA breach tickets generating ₹3.71 Lakhs in store credit liability.

### 8. What did you use AI for?
- **Tools**: Antigravity AI agent, Python pandas, Streamlit, Plotly.
- **Where helped**: Rapid exploratory data analysis, pattern identification in Freshdesk 100x scale anomaly, drafting executive memo to Arjun Mehta.
- **Threw away**: Complex heavy transformer embeddings pipeline (SentenceTransformers) which added 500MB dependencies without accuracy gains over optimized regex.
- **Screen Recording Link**: [Screen Recording Walkthrough Link - Add URL Here]

### 9. Your Public Google Drive Link
- [Insert Google Drive Link Here]

### 10. Someone picks this up on Monday and you are unreachable — 3 things they need to know
1. Legacy Freshdesk rows (`source_system == 'legacy_fd'`) must ALWAYS be divided by 100 to convert paise to INR rupees.
2. `ticket_id` contains 638 duplicate rows created during the Sept 2025 migration; deduplicate keeping `keep='first'`.
3. Returns Desk handles 78% of refunds; monitor Tier 2 vs Frontline agent assignments using `agents.csv` team mapping.

### 11. Honest hours spent
- **4.5 Hours**.

### 12. Github Repo Link
- https://github.com/OmkarKadam007/vireo-refund-intelligence
