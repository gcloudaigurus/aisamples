#This program demonstrates a simple AI application in finance: predicting stock price movement using a basic linear regression model.  This is a highly simplified example and should **not** be used for actual trading decisions. Real-world applications require far more sophisticated models, data, and risk management.


import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import yfinance as yf  # You'll need to install this: pip install yfinance

# Fetch historical stock data (replace with your desired ticker)
ticker = "AAPL"
data = yf.download(ticker, period="1y")  # Download 1 year of data

# Prepare the data
X = data[["Close"]].shift(1).dropna()  # Use yesterday's closing price to predict today's
y = data["Close"][1:]  # Today's closing price

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model (a very basic evaluation)
mse = np.mean((predictions - y_test)**2)
print(f"Mean Squared Error: {mse}")

# Example prediction for the next day (highly unreliable!)
last_close = data["Close"][-1]
next_day_prediction = model.predict([[last_close]])
print(f"Predicted closing price for tomorrow: {next_day_prediction[0]}")


#Illustrative visualization (requires matplotlib)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot(y_test.values, label='Actual')
plt.plot(predictions, label='Predicted')
plt.legend()
plt.title('Actual vs Predicted Stock Prices')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()


#**Before running:**

1#. **Install necessary libraries:**

#  pip install yfinance numpy scikit-learn matplotlib


#2. **Understand limitations:** This is a rudimentary example.  Real-world financial AI involves:

#   * **More complex models:**  Neural networks (RNNs, LSTMs), Support Vector Machines, etc., are often used.
#   * **Feature engineering:**  Using many more indicators (volume, RSI, MACD, etc.) improves accuracy.
#   * **Risk management:**  Strategies to control losses and account for uncertainty are crucial.
#   * **Robust data handling:**  Dealing with missing data, outliers, and noise.
#  * **Regulatory compliance:**  Financial models must adhere to regulations.


#This improved example provides a more complete (though still simplified) illustration of an AI application in finance. Remember that using this for actual trading is extremely risky without extensive further development and validation.  Always conduct thorough research and consider professional financial advice before making any investment decisions.
