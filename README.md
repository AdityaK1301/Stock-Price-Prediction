# Stock-Price-Prediction
This project provides a machine learning-based stock price predictor designed to forecast the end-of-day closing price of a stock using its intraday data. It includes a Jupyter notebook for data analysis and model training, as well as a Flask web application for users to interact with the model.

## Features

Data Collection: Historical stock data is fetched using yfinance.

Model Training: Several regression models are trained and evaluated, with Ridge Regression selected as the best performer.

Real-Time Prediction: A web application allows users to input a stock symbol and get a prediction of its closing price based on the latest data.

## Installation

To run this project, you need Python 3.x installed. Install the required libraries using pip:
```bash
pip install flask yfinance pandas numpy scikit-learn matplotlib seaborn joblib
```

**Note:** The web app currently uses pickle to load the model, but it is recommended to use joblib for consistency since the model was saved with joblib. Modify app.py to use joblib by changing the model loading line to:
```bash
import joblib
model = joblib.load('model.pkl')
```

## Usage

### Running the Jupyter Notebook

Open the Stock_Price_Predictor.ipynb file in Jupyter Notebook.

Run all cells to perform data analysis, model training, and evaluation. Ensure you run the cell that saves the model as model.pkl.

### Running the Web Application

Ensure the model.pkl file is in the same directory as app.py. This file is generated when you run the notebook and save the model.

Run the web application using:
```bash
python app.py
```

## Future Work

Retrain the model on data from other stocks to improve generalization.

Explore more advanced models, such as time series forecasting techniques (e.g., ARIMA, LSTM).

Enhance the web application with additional features, such as historical prediction charts or real-time data updates.
