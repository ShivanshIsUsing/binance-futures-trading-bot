# 🚀 Binance Futures Testnet Trading Bot

A Python-based trading bot that places **Market** and **Limit** orders on **Binance Futures Demo/Testnet** using a clean CLI interface, structured architecture, logging, validation, and exception handling.

## 📌 Assignment Overview

This project was built as part of the Python Developer Application Task.

### Implemented Features

✅ Place MARKET orders

✅ Place LIMIT orders

✅ Support BUY and SELL sides

✅ Binance Futures Demo/Testnet integration

✅ Command Line Interface (CLI)

✅ Interactive Menu-Based CLI (Bonus)

✅ Input Validation

✅ Exception Handling

✅ Logging of Requests, Responses, and Errors

✅ Modular Project Structure

---

# 🏗 Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd trading_bot
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

Use Binance Futures Demo/Testnet API credentials.

---

# ▶️ Running the Application

## Interactive Mode (Bonus Feature)

```bash
python cli.py
```

Example:

```text
Choose Mode:
1. Interactive Menu
2. Command Line Arguments
```

---

## Command Line Mode

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000
```

---

# 🧠 Input Validation

The application validates:

* Order Side (BUY / SELL)
* Order Type (MARKET / LIMIT)
* Quantity > 0
* Required price for LIMIT orders

Example:

```text
❌ ERROR: Side must be BUY or SELL
```

---

# 📋 Sample Output

```text
==========
ORDER RESPONSE
==========

Order ID: 13696954661
Status: NEW
Executed Qty: 0.0000
Average Price: 0.00

✅ SUCCESS
```

---

# 📊 Logging

All API requests, responses, and errors are stored in:

```text
logs/trading_bot.log
```

Example:

```text
ORDER REQUEST => {...}
ORDER RESPONSE => {...}
ORDER FAILED => ...
```

---

# 🎁 Bonus Feature Implemented

## Enhanced CLI User Experience

Features:

* Interactive menu system
* User-friendly prompts
* Validation messages
* Supports both interactive and command-line modes

Example:

```text
Choose Mode:
1. Interactive Menu
2. Command Line Arguments
```

---

# 🛡 Error Handling

The application handles:

* Invalid user input
* Binance API errors
* Missing parameters
* Authentication issues
* Network-related exceptions

---

# 🧰 Technologies Used

* Python 3.x
* python-binance
* python-dotenv
* argparse
* logging

---

# 📸 Screenshots

## Interactive CLI (Bonus Feature)

![Interactive CLI](interactive_menu.png)

---

## Successful MARKET Order

![Market Order](market_order.png)

---

## Successful LIMIT Order

![Limit Order](limit_order.png)

---

## Validation & Error Handling

![Validation](validation_error.png)

---

## Logging

![Logs](logs.png)

---

## Project Structure

![Project Structure](project_structure.png)

## Interactive CLI

Add screenshot:

```text
screenshots/interactive_menu.png
```

## Successful MARKET Order

Add screenshot:

```text
screenshots/market_order.png
```

## Successful LIMIT Order

Add screenshot:

```text
screenshots/limit_order.png
```

## Log File Output

Add screenshot:

```text
screenshots/logs.png
```

---

# 📝 Assumptions

* User has a Binance Futures Demo/Testnet account.
* Valid API credentials are provided in `.env`.
* Internet connectivity is available during execution.

---

# 👨‍💻 Author

Shivansh

Python Developer Assignment Submission
