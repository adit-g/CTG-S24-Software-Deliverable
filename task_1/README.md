# Task 1
Collecting stock data from yahoo finance and storing it in csv's
### Description
The main file in this task, collect_and_store.py, reads in stock tickers from the tickers.txt file. For each ticker, collect_and_store uses the yfinance module to get the historical stock prices and store them in a csv labelled by the ticker name. Specifically, it will collect the Volume Traded and the Open, Close, High, Low, Adjusted Close prices for each trading date.
### Usage
1. Ensure the command line is at the root level of this repository
2. Ensure that python is up to date and the yfinance module is installed
3. Simply run `python3 task_1/collect_and_store.py` and the csv's for the 25 stocks will be stored in the data folder
### Issues Encountered
The only issue I encountered with this task was finding a consistent and clean system for setting directory levels to access the tickers and data folder. I decided to just set the working directory to the repository root level at the top of the python script (in collect_and_store.py), so that everything was easily accessible.
