# Set the path to repository root level
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import getTickers, volume_adjusted_momentum
import pandas as pd

# Read in top 25 tickers
tickers = getTickers()

factor_df = pd.DataFrame()

for ticker in tickers:
    ticker_df = pd.read_csv(f'data/{ticker}.csv')
    if ticker == tickers[0]:
        factor_df['Date'] = ticker_df['Date']
    factor_df[ticker] = volume_adjusted_momentum(ticker_df, 15)

factor_df.to_csv(f'task_2/volume_adjusted_momentum/volume_adjusted_momentum.csv', index=False)