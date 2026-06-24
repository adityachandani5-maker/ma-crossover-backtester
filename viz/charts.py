import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_results(result: pd.DataFrame, ticker: str = "SPY", initial_capital: float = 10000.0):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    fig.suptitle(f"MA Crossover Strategy vs Buy & Hold — {ticker}", fontsize=14, fontweight="bold")

    buy_hold = (result["Close"] / result["Close"].iloc[0]) * initial_capital
    ax1.plot(result.index, result["total"], label="MA Crossover", color="steelblue", linewidth=1.5)
    ax1.plot(result.index, buy_hold, label="Buy & Hold", color="darkorange", linewidth=1.5, linestyle="--")
    ax1.set_ylabel("Portfolio Value ($)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    rolling_max = result["total"].cummax()
    drawdown = (result["total"] - rolling_max) / rolling_max * 100
    ax2.fill_between(result.index, drawdown, 0, color="crimson", alpha=0.4)
    ax2.set_ylabel("Drawdown (%)")
    ax2.set_xlabel("Date")
    ax2.grid(True, alpha=0.3)
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    plt.tight_layout()
    plt.savefig("results.png", dpi=150, bbox_inches="tight")
    print("Chart saved to results.png")