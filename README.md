# 📈 Quant Backtest Engine

A modular and extensible backtesting engine for systematic trading strategies, with full support for data cleaning, strategy optimization, performance visualization, and batch testing.

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/github/license/xavierchaun-lgtm/quant-backtest-engine)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/xavierchaun-lgtm/quant-backtest-engine)](https://github.com/xavierchaun-lgtm/quant-backtest-engine)

---

## 🚀 Features

- ✅ Strategy modularization (`MovingAverageCrossStrategy`)
- ✅ Custom backtesting engine (`Backtester`)
- ✅ Batch grid parameter scan with heatmaps
- ✅ Automatic parameter optimization (via `scipy.optimize`)
- ✅ Cleaned Yahoo Finance data with fallback support
- ✅ Performance metrics output (Sharpe, MDD, Annual Return)
- ✅ Auto-generated plots & markdown reports
- ✅ Easy to extend with new strategies and cost models

---
<pre>
## 📁 Project Structure

```text
QUANT BACKTEST ENGINE/
├── .venv/
├── data/
│   └── AAPL.csv
├── engine/
│   ├── backtester.py
│   ├── performance.py
│   └── demo.ipynb
├── notebooks/
├── output/
├── strategies/
│   ├── mean_reversion.py
│   ├── moving_average.py
│   ├── strategy_param_optimizer.py
│   ├── strategy_grid_scan.py
│   ├── strategy_grid_scan_batch.py
│   └── plot_grid_scan_visuals.py
├── utils/
│   └── clean_data.py
├── analyze_grid_results.py
├── main.py
├── plot_grid_scan_visuals_batch.py
├── run_batch.py
├── run_default_batch.py
├── README.md
└── requirements.txt
```
</pre>

## 🧠 Strategy Example

**Moving Average Cross Strategy**

```python
class MovingAverageCrossStrategy:
    def __init__(self, short_window, long_window):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        short_ma = data['Close'].rolling(window=self.short_window).mean()
        long_ma = data['Close'].rolling(window=self.long_window).mean()
        signals = pd.Series(0, index=data.index)
        signals[short_ma > long_ma] = 1
        signals[short_ma < long_ma] = -1
        return signals

        📊 Example Output
        <p align="center">
              <img src="output/AAPL/plot_MA_10_100_2021-2023.png" width="600"/>
        </p>
🔍 Optimization Sample
    python strategies/strategy_param_optimizer.py
Sample output:
    ✅ Optimization completed!
    Best Parameters: short_window = 10, long_window = 100
    📈 Final Sharpe Ratio: -0.0294
    📊 Full metrics saved to output/AAPL/optimized_result.csv
📦 Installation
    git clone https://github.com/xavierchaun-lgtm/quant-backtest-engine.git
    cd quant-backtest-engine
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
✅ Requirements
	•	Python 3.9+
	•	yfinance
	•	pandas, numpy
	•	matplotlib, scipy
📌 To-Do / Future Features
	•	Add transaction cost model
	•	Add stop-loss / take-profit mechanism
	•	Add RSI, MACD, Bollinger strategies
	•	Streamlit dashboard for live demo
	•	CLI & config support for batch runs

⸻

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

⸻

👨‍💻 Author

Xiaochuan Li (Xavier Chuan)
MSc Financial Engineering, University of Birmingham
GitHub: @xavierchaun-lgtm
Email: xiaochuanformal@gmail.com

⸻

⭐ If you like this project, consider giving it a star on GitHub!
