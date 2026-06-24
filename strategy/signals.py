import pandas as pd

def compute_signals(df: pd.DataFrame, short_window: int = 50, long_window: int = 200) -> pd.DataFrame:
    out = df.copy()
    out["ma_short"] = out["Close"].rolling(short_window).mean()
    out["ma_long"] = out["Close"].rolling(long_window).mean()
    out ["signal"] = 0 
    out.loc[out["ma_short"] > out["ma_long"], "signal"] = 1 
    out["position"] = out["signal"].diff()
    return out.dropna()