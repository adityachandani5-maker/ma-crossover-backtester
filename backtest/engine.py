import pandas as pd

def run_backtest(signals: pd.DataFrame, initial_capital: float = 10000.0, cost_per_trade: float = 0.001) -> pd.DataFrame:
    out = signals.copy()
    out.columns = out.columns.get_level_values(0)
    out["holdings"] = 0.0 
    out["cash"] = initial_capital
    out["total"] = initial_capital

    shares = 0.0
    cash = initial_capital

    for i in range(len(out)):
        row = out.iloc[i]
        price = float(row["Close"])

        if row["position"] == 1.0:
            shares = (cash * (1 - cost_per_trade)) / price
            cash = 0.0 
        elif row["position"] == -1.0:
            cash = shares * price * (1 - cost_per_trade)
            shares = 0.0 

        out.iloc[i, out.columns.get_loc("holdings")] = shares * price
        out.iloc[i, out.columns.get_loc("cash")] = cash
        out.iloc[i, out.columns.get_loc("total")] = shares * price + cash
    
    return out
