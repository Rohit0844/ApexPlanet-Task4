# Task 4 — Data Storytelling & Statistical Validation

**Intern:** Rohit Joshi  
**Organization:** ApexPlanet Software Pvt. Ltd.

## 1. Business objective
Combine the analysis from Tasks 1–3 into a clear business story and use a statistical method to test one business question.

## 2. Dataset snapshot
- Transaction rows: 1,000
- Distinct orders: 992
- Unique customers: 947
- Total sales: ₹139,399,439.65
- Average order value: ₹140,523.63

## 3. Business story
- Highest-revenue category: **Electronics** — ₹50,778,581.70
- Highest-revenue product: **Laptop** — ₹25,443,008.51
- Highest-revenue city: **Patna** — ₹19,285,966.89

These are descriptive results from the available data. They identify areas for business review but do not explain the causes of higher sales.

## 4. Hypothesis testing

**Business question:** Is mean total spend per customer different between Male and Female customers?

- **H₀:** Mean customer-level total spend is equal for Male and Female customers.
- **H₁:** Mean customer-level total spend is different between the two groups.

**Method:** Two-sided Welch independent-samples t-test, significance level α = 0.05. Transactions were aggregated to one total-spend value per customer before testing.

| Measure | Male | Female |
|---|---:|---:|
| Customers | 502 | 479 |
| Mean spend per customer | ₹144,349.70 | ₹139,740.90 |
| Standard deviation | ₹118,437.46 | ₹117,866.23 |

- Mean difference (Male − Female): ₹4,608.81
- Welch t-statistic: 0.6107
- Welch degrees of freedom: 977.27
- p-value: 0.5415
- 95% confidence interval: ₹-10,199.94 to ₹19,417.56

### Conclusion
Because p = 0.5415 is greater than 0.05, we **fail to reject H₀**. This dataset does not provide sufficient statistical evidence at the 5% significance level that mean customer-level spend differs between Male and Female customers. The 95% confidence interval includes zero. This does not prove that the groups are identical.

## 5. Business recommendations
1. Continue monitoring category, product and city performance.
2. Do not make marketing decisions based only on gender using this test.
3. Collect longer customer histories and richer business context before making retention or lifetime-value decisions.
4. Repeat the analysis as new data becomes available.

## 6. Limitations
- Observational transaction data, not a randomized experiment.
- Customer spending may be skewed; the t-test compares means.
- Test includes customers with Male or Female gender values only.
- Findings apply to this dataset and period, not necessarily all customers.
- The source has no website funnel events or marketing exposure fields.

## 7. Reproducibility
Install dependencies and run:
```bash
pip install -r requirements.txt
python analysis/task4_analysis.py
```
