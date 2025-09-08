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

## 📂 Project Structure
QUANT BACKTEST ENGINE/
├── .venv/                        # ✅ Virtual environment (should be excluded from GitHub)
│                                # 虚拟环境文件夹（建议添加到 .gitignore，不上传）
│
├── data/
│   └── AAPL.csv                  # ✅ Example raw data (used as fallback if yfinance unavailable)
│                                # 示例数据文件（如无法下载数据时使用）
│
├── engine/
│   ├── backtester.py            # ✅ Core backtest engine logic
│   ├── performance.py           # ✅ Performance metrics (e.g., Sharpe, Max Drawdown)
│   └── demo.ipynb               # ✅ (Optional) demo notebook — recommended to move to notebooks/
│                                # 回测引擎核心逻辑模块、绩效指标计算
│
├── notebooks/                   # ✅ Jupyter notebooks for interactive testing or analysis
│                                # Jupyter 笔记本目录（可选，用于交互式测试）
│
├── output/                      # ✅ Auto-generated results: plots, CSVs, metrics
│                                # 自动生成的结果文件，如图像、CSV 指标表等
│
├── strategies/                  # ✅ Strategy implementations & parameter tools
│   ├── mean_reversion.py        #   Mean Reversion Strategy | 均值回复策略
│   ├── moving_average.py        #   Moving Average Strategy | 均线策略
│   ├── strategy_param_optimizer.py   #   Optimize strategy parameters (maximize Sharpe)
│   ├── strategy_grid_scan.py         #   Grid scan tool | 网格扫描主程序
│   ├── strategy_grid_scan_batch.py   #   Batch grid scan for multiple tickers | 多标的网格扫描
│   └── plot_grid_scan_visuals.py     #   Generate heatmaps or 3D plots | 生成可视化图像
│
├── utils/
│   └── clean_data.py            # ✅ Clean and standardize downloaded data
│                                # 数据清洗模块（列名展平、缺失处理等）
│
├── analyze_grid_results.py      # ✅ Analyze grid scan results (e.g., best Sharpe per ticker)
│                                # 网格扫描结果分析脚本
│
├── main.py                      # ✅ Main entry script (can rename to run_strategy.py)
│                                # 主运行脚本（可重命名为 run_strategy.py）
│
├── plot_grid_scan*.py           # ✅ (Optional) Individual plotting scripts
│                                # 图像绘制脚本（建议集中移入 scripts/ 或保持统一风格）
│
├── run_batch.py                 # ✅ Run multiple strategies/tickers in batch mode
│   run_default_batch.py         # ✅ Use default parameters to run one or more strategies
│                                # 批量运行或默认参数测试脚本
│
├── README.md                    # ✅ Project documentation & instructions
│                                # 项目说明文档
│
├── requirements.txt             # ✅ Required Python dependencies
│                                # 所需 Python 依赖列表
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