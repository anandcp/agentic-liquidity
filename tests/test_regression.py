import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

def test_regression_runs():
    df = pd.DataFrame({
        "Lg": np.linspace(0.1, 0.9, 20),
        "contributor_growth": np.random.normal(0, 0.05, 20),
        "Lg2": np.linspace(0.1, 0.9, 20)**2,
        "org_flag": np.zeros(20),
        "age_months": np.arange(1, 21)
    })

    model = smf.ols(
        formula="contributor_growth ~ Lg + Lg2 + org_flag + age_months",
        data=df
    ).fit()

    assert "Lg" in model.params
    assert "Lg2" in model.params

    a = model.params["Lg2"]
    b = model.params["Lg"]
    turning_point = -b / (2 * a)

    assert np.isfinite(turning_point)