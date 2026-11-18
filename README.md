# ApexPlanet Task 4 — Data Storytelling & Statistical Validation

**Author:** Rohit Joshi

## Included
- `presentation/ApexPlanet_Task4_Final_Presentation.pptx` — final stakeholder presentation
- `analysis/Task4_Hypothesis_Testing_Summary.md` — business story and test interpretation
- `analysis/Task4_Statistical_Results.xlsx` — group statistics and hypothesis test
- `analysis/task4_analysis.py` — reproducible Python analysis
- `analysis/Task4_LinkedIn_Video_Script.md` — 7–10 minute video script
- `data/cleaned_sales_dataset.csv` — cleaned dataset
- `charts/` — supporting visualizations

## Hypothesis
Is mean customer-level total spend different between Male and Female customers? Welch independent-samples t-test, two-sided, alpha 0.05.

## Result
p-value = 0.5415; 95% CI = ₹-10,200 to ₹19,418. Fail to reject H0. This dataset does not provide sufficient evidence of a difference in the group means.

## Run
```bash
pip install -r requirements.txt
python analysis/task4_analysis.py
```

Suggested public GitHub repository: `Rohit-Joshi-ApexPlanet-Task4`

This is observational data. Do not claim causation or generalize beyond the dataset.
