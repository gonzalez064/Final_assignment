import pandas as pd
from src.analysis import compute_correlation

def test_compute_correlation():
    data = {
        "Income": [1000, 2000, 3000, 4000],
        "LifeExpectancy": [70, 75, 80, 85]
    }
    df = pd.DataFrame(data)
    corr = compute_correlation(df)
    assert round(corr, 2) == 1.00
