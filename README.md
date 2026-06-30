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



