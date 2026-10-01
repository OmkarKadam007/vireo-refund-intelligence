To: Arjun Mehta, Finance Controller

From: Vireo Refund Intelligence Team

Date: 1 October 2026

Subject: Resolution of the ₹1 Crore Refund Variance and GW-OTHER Misclassification

The actual support refund volume is operating stably at ~₹11.18 Lakh per quarter. The >₹1 Crore figure in the Finance export is the result of two structural data errors stemming from the September 2025 system migration, compounded by a behavioral reporting issue on the frontline.

1. The 1 Crore vs 11 Lak Data Bug
The raw helpdesk export contains two critical reporting flaws:

Currency Unit Mismatch: The legacy Freshdesk system (legacy_fd) stored monetary values in paise, while the new helpdesk stores them in rupees. When combined in the raw export, legacy refunds appear 100x larger than reality (e.g., a ₹900 refund is logged as 90,000).

Migration Duplication: 1,276 tickets were imported twice during the transition, meaning Finance is double-counting these specific liabilities.

Resolution: After deduplicating the overlapping tickets and converting legacy paise values to rupees, the true total refund volume across the 18-month dataset is verified at ₹6,709,932 (approx. ₹11.18 Lakh/quarter).

2. The GW-OTHER Behavioral Issue (Why refunds look unexplainable)
While the total amount is correct, visibility into why money is leaving the business has been obscured. 991 refund tickets (accounting for ₹22 Lakh, or 33% of total refunds) were tagged by agents as GW-OTHER (Goodwill/Other).

Because GW-OTHER is the first option in the reason-code dropdown, agents are selecting it as a default to close tickets quickly, masking the true operational reasons.

3. Remediation and Recovered Visibility
We deployed a deterministic NLP text-matching engine to analyze the unstructured customer messages and agent closing notes for all 991 GW-OTHER tickets.

We successfully re-classified 533 of these tickets (over 53%) into their correct categories.

The analysis proves agents are not arbitrarily giving away free money.The hidden refunds were predominantly standard operational scenarios: an additional ₹4 Lakh was actually RETURN-QC-OK, and ₹3 Lakh was DUP-PAYMENT.

True GW-OTHER exposure is significantly lower than previously reported.

To prevent this moving forward, we recommend removing GW-OTHER as the default first option in the helpdesk UI and mandating a secondary text-validation rule for any refund exceeding ₹500.