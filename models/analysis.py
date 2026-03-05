import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Calculate total expense
    df["Total_Expense"] = df.iloc[:, 2:].sum(axis=1)

    # Calculate savings
    df["Savings"] = df["Income"] - df["Total_Expense"]

    # Savings ratio
    df["Savings_Ratio"] = df["Savings"] / df["Income"]

    return df