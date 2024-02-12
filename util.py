def getTickers():
    with open('task_1/tickers.txt', 'r') as f:
        tickers = f.read().splitlines()

    # Ensure all tickers were read in
    if len(tickers) != 25:
        print('ERROR: Tickers not read in correctly')

    return tickers

def calculate_momentum(df, n):
    return (df['Close'].shift(1) - df['Close'].shift(n+1)) / df['Close'].shift(n+1) * 100

def volume_adjusted_momentum(df, n):
    return calculate_momentum(df, n) / df['Volume'].shift(1)

def win_loss_ratio(df, n):
    rtns = df['Close'] / df['Close'].shift(1) - 1
    rtns = rtns.shift(1)

    def calculate_ratio(window):
        win = 0
        loss = 0
        for rtn in window:
            if rtn > 0:
                win += rtn
            elif rtn < 0:
                loss += -1 * rtn
        return win / loss
    
    return rtns.rolling(n).apply(calculate_ratio)