# GOLD AI TRADING SYSTEM

## Introduction

Gold AI Trading System là một hệ thống AI giao dịch được xây dựng bằng Python dành cho MetaTrader 5.

Mục tiêu của dự án là tạo ra một nền tảng giao dịch thông minh có khả năng:

- Theo dõi thị trường theo thời gian thực.
- Phân tích dữ liệu đa khung thời gian.
- Kết hợp Indicator + Smart Money Concept (SMC).
- Tự động đánh giá xu hướng.
- Đưa ra quyết định BUY / SELL / HOLD.
- Quản lý rủi ro.
- Gửi tín hiệu Telegram.
- Tự động giao dịch trên MT5.
- Học từ dữ liệu lịch sử để cải thiện hiệu suất.

---

# Main Features

## Market

- Connect MetaTrader5
- Load Historical Data
- Real-Time Candle Monitoring
- Tick Monitoring
- Market Status

---

## Indicators

- EMA
- RSI
- ATR
- ADX
- MACD
- Bollinger Bands
- VWAP
- SuperTrend
- Volume

---

## Smart Money Concept

- BOS
- CHOCH
- Order Block
- Breaker Block
- Mitigation Block
- Liquidity
- Liquidity Sweep
- Fair Value Gap
- Inverse Fair Value Gap
- Market Structure

---

## Trend Analysis

- Multi Timeframe Analysis
- Market Bias
- Trend Direction
- Pullback Detection
- Sideway Detection

---

## AI Decision

AI sẽ tổng hợp dữ liệu từ:

- Indicators
- Smart Money Concept
- Trend
- Session
- Spread
- Volume

Sau đó đưa ra:

- BUY
- SELL
- HOLD

Đồng thời trả về:

- Confidence Score
- Entry
- Stop Loss
- Take Profit
- Risk Reward
- Reason

---

## Risk Management

- Dynamic Lot Size
- Daily Loss Limit
- Daily Profit Limit
- Spread Filter
- Drawdown Protection
- Risk Per Trade

---

## Signal System

Bot có thể gửi thông báo:

- New Signal
- Buy Signal
- Sell Signal
- Entry Filled
- Stop Loss
- Take Profit
- Break Even
- Trailing Stop
- Daily Report
- Weekly Report

---

## Auto Trading

Nếu được bật, bot sẽ:

- Open Position
- Modify Position
- Close Position
- Partial Close
- Trailing Stop
- Break Even

---

## Dashboard

Dashboard hiển thị:

- Balance
- Equity
- Profit
- Drawdown
- Win Rate
- Active Trades
- Market Trend
- AI Confidence
- Current Session

---

# Project Structure

```text
gold_ai/
│
├── core/
├── indicators/
├── smc/
├── trend/
├── strategy/
├── ai/
├── execution/
├── risk/
├── notify/
├── dashboard/
├── database/
├── models/
├── tests/
├── logs/
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Workflow

```text
Start

↓

Connect MT5

↓

Load Candle History

↓

Build Cache

↓

Wait New Candle

↓

Indicators

↓

SMC

↓

Trend

↓

Risk Check

↓

AI Decision

↓

BUY / SELL / HOLD

↓

Signal

↓

Telegram

↓

Dashboard

↓

Auto Trade

↓

Database

↓

Learning

↓

Repeat
```

---

# Coding Standard

- Python 3.12+
- PEP8
- OOP
- Type Hint
- Google Style Docstring
- Modular Design
- Clean Architecture
- Event Driven
- Logging
- Exception Handling

---

# Future Roadmap

- Backtesting Engine
- Machine Learning Optimization
- Portfolio Management
- Multi Symbol Trading
- Multi Broker Support
- Web Dashboard
- Mobile Notification
- Cloud Deployment

---

# Version

Current Version

```
v1.0
```

---

# Author

Gold AI Trading System Project