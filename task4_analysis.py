from pathlib import Path
import pandas as pd
import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "cleaned_sales_dataset.csv")
customer = df.groupby(["Customer_ID","Gender"])["Total_Sales"].sum().reset_index()
male = customer.loc[customer.Gender=="Male","Total_Sales"].dropna()
female = customer.loc[customer.Gender=="Female","Total_Sales"].dropna()
result = stats.ttest_ind(male, female, equal_var=False)
v1, v2 = male.var(ddof=1)/len(male), female.var(ddof=1)/len(female)
se = np.sqrt(v1+v2)
dfw = (v1+v2)**2 / (v1**2/(len(male)-1) + v2**2/(len(female)-1))
diff = male.mean()-female.mean()
crit = stats.t.ppf(.975,dfw)
out = pd.DataFrame([{"t_statistic":result.statistic,"df":dfw,"p_value":result.pvalue,
 "mean_difference_male_minus_female":diff,"ci95_lower":diff-crit*se,
 "ci95_upper":diff+crit*se,"alpha":0.05}])
out.to_csv(ROOT/"analysis"/"hypothesis_test_results.csv",index=False)
print(out.to_string(index=False))
