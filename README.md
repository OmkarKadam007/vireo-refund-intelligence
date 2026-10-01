# Vireo Audio — Support Refund Intelligence & Reconciliation Tool

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/framework-Streamlit-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An AI-assisted, zero-cost support data reconciliation and analytics dashboard built for **Vireo Audio Pvt. Ltd.** to audit support ticket exports, reconcile multi-crore financial variances for the Board Pack, identify frontline agent misclassification, and detect cost-leakage policy violations.

---

## 🎯 Key Executive Summary & Findings

Finance Controller Arjun Mehta reported an alarming quarterly refund export exceeding **₹3.8 Crore/quarter** (~₹23 Crore over 18 months). 

Our automated data audit uncovered **4 structural data & operational anomalies**:

1. **Legacy Currency Scaling Bug (100x Inflation)**:
   - Freshdesk legacy tickets (`source_system == 'legacy_fd'`) stored monetary values in **paise**. 
   - Converting legacy monetary amounts to INR rupees reduces total 18-month refunds from ₹23 Crore down to **₹67.09 Lakhs (₹11.18 Lakhs/quarter)**, perfectly reconciling Finance's export with Helpdesk Admin expectations (~₹11 Lakh/quarter).
2. **Migration Duplicates**:
   - **638 tickets** were double-imported during the September 2025 helpdesk migration. Deduplication eliminates double-counted liabilities.
3. **GW-OTHER Misclassification (43.3% Exposure)**:
   - Frontline agents over-used `GW-OTHER` (Goodwill/Other) as it was the default first option in the helpdesk dropdown. 
   - Our deterministic NLP rule engine re-classified **53.8%** of GW-OTHER refunds back into true operational categories (Dead on Arrival, Return QC Passed, Duplicate Payments), reducing unclassified Goodwill from 43.3% down to 20.3%.
4. **Double-Dipping & SLA Leakages**:
   - **166 Tickets** received **BOTH a refund and a replacement** for the same order (Violation of Policy §5), causing **₹8.71 Lakhs** in direct financial leakage.
   - **1,060 Tickets** breached SLA first-response targets, accumulating **₹3.71 Lakhs** in store credit liability (@ ₹350/ticket).

---

## 📊 Reconciled Financial Summary

| Metric | Raw Helpdesk Export | Reconciled Verified Value | Root Cause / Resolution |
| :--- | :--- | :--- | :--- |
| **18-Month Refunds** | ₹23,01,24,081 | **₹67,09,932** | 100x Paise-to-Rupee scaling + 638 duplicate rows fixed |
| **Quarterly Run-Rate** | ₹3,83,54,013 | **₹11,18,322** | Reconciled for Board Pack (Exact match to Helpdesk Admin) |
| **GW-OTHER Exposure** | ₹29,07,036 (43.3%) | **₹13,66,306 (20.3%)** | 53.8% re-classified via NLP rule engine |
| **Double-Dipping Loss** | Untracked | **166 Tickets (₹8.71 L)** | Simultaneous refund + replacement issued |
| **SLA Credit Liability** | Untracked | **1,060 Tickets (₹3.71 L)** | ₹350 store credit liability per delayed first response |

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10 or higher

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/vireo-refund-intelligence.git
   cd vireo-refund-intelligence
   ```

2. **Create and activate virtual environment**:
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit Dashboard**:
   ```bash
   streamlit run main.py
   ```

---

## 📁 Repository Structure

```
vireo-refund-intelligence/
├── data/
│   ├── raw/                  # CSV datasets (tickets.csv, agents.csv, orders.csv, products.csv, customers.csv)
│   └── reference/            # Policy documents, email threads, submission form
│       ├── support-policy.pdf
│       ├── email-thread.txt
│       └── submission-form.md
├── notebooks/
│   └── 01_data_understanding.ipynb   # Exploratory Data Analysis & Validation
├── reports/
│   └── memo_to_arjun.md      # 1-Page Executive Board Pack Memo
├── src/                      # Modular Python utilities
│   ├── analysis/
│   ├── config/
│   ├── data/
│   └── utils/
├── .gitignore                # Production gitignore rules
├── main.py                   # Main Streamlit Dashboard Application
├── README.md                 # Project Documentation
└── requirements.txt          # Dependencies
```

---

## 💡 Key Deliverables

- **Executive Board Pack Memo**: Located at [`reports/memo_to_arjun.md`](reports/memo_to_arjun.md)
- **Official Submission Form**: Located at [`data/reference/submission-form.md`](data/reference/submission-form.md)

---

## 📄 License
This project is licensed under the MIT License.
