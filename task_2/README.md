# Task 2
This task involved calculating some factors and storing them in csv's
### Description
In 3 separate folders, I calculated 3 different factors that could be used to assess a stock's outlook on a given day. The first two factors, price momentum and volume adjusted momentum, were given. For the third factor, I came up with a win/loss ratio, which takes the ratio between the average winning return and the average losing return over a given period of time. I felt that this metric could gauge how many losing bets a winning bet could cover. I had a few other ideas for my third factor, but I went with this one because it generated a phenomenal 240% return over the given time period.
### Usage
Assuming pandas is installed, just run `python3 task_2/{factor_name}/{factor_name}.py`, substituting 'factor_name' for either price_momentum, volume_adjusted_momentum, or win_loss_ratio. This will generate the csv in the same folder as the python script being run.
