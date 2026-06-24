import sys
sys.path.insert(0, '.')

from data.loader import fetch_prices
from strategy.signals import compute_signals
from backtest.engine import run_backtest
from metrics.stats import compute_metrics
from viz.charts import plot_results

TICKER = "SPY"
START = "2015-01-01"
END = "2024-01-01"
INITIAL_CAPITAL = 10000.0

print(f"Running MA Crossover Backtest on {TICKER} from {START} to {END}")
print("-" * 55)

df = fetch_prices(TICKER, START, END)
signals = compute_signals(df)
result = run_backtest(signals, initial_capital=INITIAL_CAPITAL)
metrics = compute_metrics(result, initial_capital=INITIAL_CAPITAL)
plot_results(result, ticker=TICKER, initial_capital=INITIAL_CAPITAL)

print("\nPerformance Metrics:")
print(f"  {'Metric':<25} {'Strategy':>12} {'Buy & Hold':>12}")
print("  " + "-" * 49)
for metric in metrics["strategy"]:
    s = metrics["strategy"][metric]
    b = metrics["buy_and_hold"][metric]
    print(f"  {metric:<25} {str(s):>12} {str(b):>12}")
