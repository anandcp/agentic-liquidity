import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("../data/sample_repo_panel.csv")
df["Lg2"] = df["Lg"] ** 2

model = smf.ols(
    formula="contributor_growth ~ Lg + Lg2 + org_flag + age_months",
    data=df,
)
res = model.fit()

print(res.summary())

b1 = res.params["Lg"]
b2 = res.params["Lg2"]

L_star = -b1 / (2 * b2)
print(f"Turning point L*: {L_star:.3f}")