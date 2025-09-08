import pandas as pd
import matplotlib.pyplot as plt

class Backtester:
    def __init__(self, data, strategy):
        self.data = data  # 自动清洗数据
        self.strategy = strategy
        self.signals = None
        self.returns = None
        self.total_return = None
        self.annual_return = None
        self.max_drawdown = None
        self.sharpe_ratio = None

    def run(self):
        self.signals = self.strategy.generate_signals(self.data)
        self.returns = self.data['Close'].pct_change().shift(-1) * self.signals

        self.total_return = self.returns.sum()
        self.annual_return = self.returns.mean() * 252
        self.max_drawdown = self.calculate_max_drawdown()
        self.sharpe_ratio = self.returns.mean() / self.returns.std() * (252 ** 0.5)

    def calculate_max_drawdown(self):
        cum_returns = (1 + self.returns.fillna(0)).cumprod()
        rolling_max = cum_returns.cummax()
        drawdown = (cum_returns - rolling_max) / rolling_max
        return drawdown.min()

    def plot(self, ticker, strategy_name, start_date, end_date):
        cum_returns = (1 + self.returns.fillna(0)).cumprod()
        cum_returns.plot(title=f"{ticker} | {strategy_name} | {start_date} to {end_date}")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Return")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"output/plot_{ticker}_{strategy_name}_{start_date[:4]}-{end_date[:4]}.png")
        plt.close()

    def save_metrics(self, path):
        metrics = {
            "Total Return": [self.total_return],
            "Annualized Return": [self.annual_return],
            "Max Drawdown": [self.max_drawdown],
            "Sharpe Ratio": [self.sharpe_ratio]
        }
        df = pd.DataFrame(metrics)
        df.to_csv(path, index=False)