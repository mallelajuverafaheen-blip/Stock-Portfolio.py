# 📈 Stock Portfolio Tracker | Python Project

### 💻 Developed as Part of the CodeAlpha Python Programming Task

## 📌 Project Overview

The **Stock Portfolio Tracker** is a simple Python application that calculates the total investment value of stocks based on predefined stock prices and user-entered quantities.

This project demonstrates essential Python programming concepts, including dictionaries, loops, conditional statements, functions, input validation, arithmetic operations, and CSV file handling.

Users can select stocks, enter quantities, view individual investment values, calculate their total investment, and optionally save their portfolio details to a CSV file.

## 🎯 Objectives

* Calculate the investment value of individual stocks.
* Determine the total investment value of a portfolio.
* Use a Python dictionary to store predefined stock prices.
* Accept and validate user input.
* Display a clear portfolio summary.
* Save portfolio details using CSV file handling.

## ✨ Key Features

* 📊 **Predefined Stock Prices:** Stores stock symbols and prices in a Python dictionary.
* 🧮 **Automatic Calculations:** Calculates investment values based on stock prices and quantities.
* 💰 **Portfolio Summary:** Displays individual investments and the total investment value.
* ✅ **Input Validation:** Handles invalid stock symbols and quantities.
* 📁 **CSV Export:** Saves portfolio details to a CSV file.
* 🖥️ **Command-Line Interface:** Provides a simple, interactive user experience.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Code Editor:** Visual Studio Code (VS Code)
* **Data Structure:** Dictionary and List
* **File Handling:** CSV module
* **Error Handling:** Try-except statements

## 📋 Predefined Stock Prices

The application includes the following example stock prices:

| Stock Symbol | Price per Share |
| ------------ | --------------: |
| AAPL         |         $180.00 |
| TSLA         |         $250.00 |
| GOOGL        |         $140.00 |
| MSFT         |         $420.00 |
| AMZN         |         $190.00 |
| NVDA         |         $120.00 |
| META         |         $500.00 |

**Note:** These are hardcoded example prices for educational purposes. They are not live market prices.

## ⚙️ Installation and Setup

### Step 1: Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

### Step 2: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your actual GitHub repository.

### Step 3: Open the Project Folder

```bash
cd Stock-Portfolio-Tracker
```

### Step 4: Run the Application

```bash
python stock_portfolio_tracker.py
```

On Windows, you can also try:

```bash
py stock_portfolio_tracker.py
```

**Requirements:** Python 3 and no additional external packages.

## ▶️ How to Use

1. Run the Python program.
2. View the available stock symbols and their predefined prices.
3. Enter a stock symbol, such as `AAPL`.
4. Enter the quantity of shares.
5. Repeat the process to add more stocks.
6. Enter `DONE` to finish entering stocks.
7. View the portfolio summary and total investment value.
8. Choose whether to save the portfolio to a CSV file.

## 🧮 Calculation Method

The program uses the following formula:

**Individual Investment Value**

Investment Value = Stock Price × Quantity

**Total Portfolio Investment**

Total Investment = Sum of All Individual Investment Values

### Example

Suppose a user enters:

* AAPL: 10 shares at $180 per share
* TSLA: 5 shares at $250 per share

Calculations:

* AAPL Investment = 10 × $180 = $1,800
* TSLA Investment = 5 × $250 = $1,250

**Total Investment = $3,050**

## 📊 Sample Output

```text
==================================================
          STOCK PORTFOLIO TRACKER
==================================================

Enter stock symbol (or DONE to finish): AAPL
Enter quantity of AAPL: 10

AAPL added successfully!
Investment value: $1800.00

Enter stock symbol (or DONE to finish): TSLA
Enter quantity of TSLA: 5

TSLA added successfully!
Investment value: $1250.00

Enter stock symbol (or DONE to finish): DONE

                 PORTFOLIO SUMMARY

Stock       Quantity    Price ($)      Investment ($)
-----------------------------------------------------
AAPL        10          180.00         1800.00
TSLA        5           250.00         1250.00
-----------------------------------------------------
TOTAL INVESTMENT: $3050.00

Save portfolio to CSV file? (yes/no): yes

Portfolio saved successfully to stock_portfolio.csv!
```

*The sample output illustrates the calculation using predefined example prices.*

## 📁 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio_tracker.py
├── README.md
├── .gitignore
└── stock_portfolio.csv  # Generated when the portfolio is saved
```

## 🧠 Python Concepts Learned

| Concept                | Application                                      |
| ---------------------- | ------------------------------------------------ |
| Dictionary             | Stores stock symbols and prices                  |
| Variables              | Stores quantities, prices, and investment values |
| User Input             | Accepts stock symbols and quantities             |
| Loops                  | Supports multiple stock entries                  |
| Conditional Statements | Validates stock symbols and quantities           |
| Functions              | Organizes code into reusable blocks              |
| Lists                  | Stores portfolio entries                         |
| Arithmetic Operations  | Calculates investment values                     |
| Exception Handling     | Handles invalid inputs and file errors           |
| File Handling          | Saves portfolio data in CSV format               |

## 🚀 Future Enhancements

The project can be improved by adding:

* 📡 Live stock prices through a market data API.
* 📈 Interactive portfolio charts and graphs.
* 💹 Profit and loss calculations.
* 🗄️ Database integration for persistent portfolio storage.
* 🖥️ A graphical user interface.
* 👤 User accounts and multiple portfolio management.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Applying Python fundamentals to solve a real-world-inspired problem.
* Working with dictionaries and lists.
* Performing calculations using user-provided data.
* Implementing input validation and exception handling.
* Saving structured data using CSV file handling.
* Organizing and testing a Python application.

## 👩‍💻 Project Information

**Project Name:** Stock Portfolio Tracker
**Organization:** CodeAlpha
**Domain:** Python Programming
**Language:** Python
**Development Environment:** Visual Studio Code

## ⚠️ Disclaimer

This project is intended for educational purposes only. Stock prices are predefined example values and do not represent live market prices. The application does not provide financial advice.

---

⭐ **If you find this project useful, consider giving the repository a star!**

**Learning by Building | Improving Through Practice | Growing with Python**
