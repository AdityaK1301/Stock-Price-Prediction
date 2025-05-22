from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import yfinance as yf
import pickle

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load('/model.pkl')

# Function to fetch stock data
def get_stock_data(stock_symbol):
    data = yf.download(stock_symbol, period='1y')
    return data

# Function to predict stock price
def predict_stock_price(stock_symbol):
    data = get_stock_data(stock_symbol)
    if data.empty:
        return None
    
    # Feature selection
    data = data[['Open', 'High', 'Low', 'Volume']].dropna()
    
    # Predict
    prediction = model.predict([data.iloc[-1].values])[0]  # Predict using the latest available data
    return prediction

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    stock_symbol = ""
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        prediction = predict_stock_price(stock_symbol)
    
    return render_template('templates/index.html', prediction=prediction, stock_symbol=stock_symbol)

if __name__ == '__main__':
    app.run(debug=True)