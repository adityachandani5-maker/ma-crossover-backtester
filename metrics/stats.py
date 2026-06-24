import pandas as pd
import numpy as np

def compute_metrics(result: pd.DataFrame, initial_capital: float = 10000.0, risk_free_rate: float = 0.04) -> dict:
    total = result["total"]
    daily_returns = total.pct_change().dropna()

    total_return = (total.iloc[-1] / total.iloc[0]) - 1
    n_years = len(total) / 252
    annualized_return = (1 + total_return) ** (1 / n_years) - 1
    excess_returns = daily_returns - (risk_free_rate / 252)
    sharpe = (excess_returns.mean() / excess_returns.std()) * (252 ** 0.5)
    rolling_max = total.cummax()
    drawdown = (total - rolling_max) / rolling_max
    max_drawdown = drawdown.min()

    bh = (result["Close"] / result["Close"].iloc[0]) * initial_capital
    bh_returns = bh.pct_change().dropna()
    bh_total_return = (bh.iloc[-1] / bh.iloc[0]) - 1
    bh_annualized = (1 + bh_total_return) ** (1 / n_years) - 1
    bh_excess = bh_returns - (risk_free_rate / 252)
    bh_sharpe = (bh_excess.mean() / bh_excess.std()) * (252 ** 0.5)
    bh_drawdown = ((bh - bh.cummax()) / bh.cummax()).min()

    return {
        "strategy": {
            "Total Return (%)": round(total_return * 100, 2),
            "Annualized Return (%)": round(annualized_return * 100, 2),
            "Sharpe Ratio": round(sharpe, 3),
            "Max Drawdown (%)": round(max_drawdown * 100, 2),
        },
        "buy_and_hold": {
            "Total Return (%)": round(bh_total_return * 100, 2),
            "Annualized Return (%)": round(bh_annualized * 100, 2),
            "Sharpe Ratio": round(bh_sharpe, 3),
            "Max Drawdown (%)": round(bh_drawdown * 100, 2),
        }
    }

    