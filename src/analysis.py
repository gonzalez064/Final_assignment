import pandas as pd

def load_data(life_path, income_path):
    df_life = pd.read_csv(life_path, sep=";", encoding="latin1")
    df_income = pd.read_csv(income_path, sep=";", encoding="latin1")
    return df_life, df_income


def prepare_data(df_life, df_income):
    df_life.columns = ["Province", "Year", "LifeExpectancy"]
    df_income.columns = ["Province", "Year", "Income"]

    df = pd.merge(df_life, df_income, on=["Province", "Year"])


    df["LifeExpectancy"] = (
        df["LifeExpectancy"]
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    df["LifeExpectancy"] = pd.to_numeric(df["LifeExpectancy"], errors="coerce")

    df["Income"] = (
        df["Income"]
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    df["Income"] = pd.to_numeric(df["Income"], errors="coerce")

    df = df.dropna(subset=["Income", "LifeExpectancy"])

    return df

def compute_correlation(df):
    return df["Income"].corr(df["LifeExpectancy"])

