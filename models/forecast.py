from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_expense(df):
    df = df.reset_index()

    X = df.index.values.reshape(-1, 1)
    y = df["Total_Expense"].values

    model = LinearRegression()
    model.fit(X, y)

    # Predict next month
    next_month = np.array([[len(df)]])
    prediction = model.predict(next_month)

    return round(prediction[0], 2)