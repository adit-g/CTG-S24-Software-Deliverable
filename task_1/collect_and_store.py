# Set the path to repository root level
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import getTickers
import yfinance as yf

# Read in tickers from helper method in util.py
tickers = getTickers()

START = '2021-01-01'
END = '2024-01-01'
DATA_LENGTH = 753

for t in tickers:
    df = yf.download(t, start=START, end=END)

    # Ensure the data frames got every single date
    if len(df) != DATA_LENGTH:
        print(f'ERROR: Ticker {t} does not have the correct number of days')

    # Ensure there are no missing values
    if df.isnull().any().any():
        print(f'ERROR: Ticker {t} contains missing values')

    df.to_csv(f'data/{t}.csv')