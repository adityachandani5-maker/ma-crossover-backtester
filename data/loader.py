import yfinance as yf
import pandas as pd

def fetch_prices(ticker: str, start: str, end: str) -> pd.DataFrame:
    raw = yf.download(ticker, start = start, end = end, auto_adjust=True)
    df = raw[["Close"]].copy()
    df.index = pd.to_datetime(df.index)
    return df