# Moving-Average Crossover Backtester

A rigorous backtesting engine for a dual moving-average crossover strategy, built with no lookahead bias, real transaction costs, and honest benchmarking against buy-and-hold.

## Project Structure
```
ma-crossover-backtester/
├── data/           # Data fetching and preprocessing
├── strategy/       # Signal generation
├── backtest/       # Position sizing and P&L engine
├── metrics/        # Performance statistics
├── viz/            # Equity curve and drawdown charts
├── tests/          # Unit tests
└── notebooks/      # Exploratory analysis
```

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Methodology Notes
- **No lookahead bias**: signals computed at close of day t; position applied from day t+1.
- **Transaction costs**: round-trip cost subtracted on every position change.
- **Benchmark**: all results shown against buy-and-hold of the same asset.

## Results
Backtest period: 2015-01-01 to 2024-01-01 | Asset: SPY | Starting capital: $10,000

| Metric               | MA Crossover | Buy & Hold |
|----------------------|-------------|------------|
| Total Return (%)     | 89.33       | 170.84     |
| Annualized Return (%)| 8.10        | 12.93      |
| Sharpe Ratio         | 0.330       | 0.538      |
| Max Drawdown (%)     | -33.72      | -33.72     |

The strategy successfully avoided the 2022 rate-hike drawdown by moving to cash,
but failed to dodge the March 2020 COVID crash due to the slow reaction time of
the 200-day moving average. Over the full period, buy & hold outperformed on both
absolute and risk-adjusted terms.

## Limitations
- **Slow signals**: the 200-day MA reacts too slowly to sudden market dislocations
  (e.g. COVID crash). The strategy is better suited to slow-moving bear markets.
- **Opportunity cost**: sitting in cash during bull markets (e.g. 2015-2019 recovery)
  significantly drags on returns relative to buy & hold.
- **Single asset**: tested only on SPY. Results may differ on individual stocks,
  which have higher volatility and less mean-reverting behavior.
- **No parameter optimization**: short/long window sizes (50/200) were chosen by
  convention, not by optimization. Optimizing on this dataset would introduce
  lookahead bias.

## What I'd Do Differently
Starting over, I'd change three things. 

- First, I'd stop treating a single backtest on a single asset as meaningful evidence — one clean-looking result on SPY proves almost nothing, so I'd test across multiple assets and distinct market regimes (e.g. a sideways decade like the 2000s, not just the 2015–2024 bull market) to see whether the strategy holds up or whether I just got a flattering window.
-  Second, I'd build out-of-sample / walk-forward validation from the start rather than reporting in-sample numbers, since the real question isn't "did this work on history" but "would it have worked on data I hadn't seen."
-  Third, I'd separate the signal logic from the cost and execution assumptions more cleanly, so I could stress-test slippage and transaction-cost sensitivity independently instead of baking one fixed assumption into the engine.
-  More broadly, the project taught me to be suspicious of my own results. The most useful output here wasn't the strategy — it was confirming that a conventional, un-optimized MA crossover underperforms, which is a more honest finding than a tuned strategy that looks good only because it was fit to the same data I tested it on.



