# ==================================================
# CodeAlpha Python Programming Task
# Project: Stock Portfolio Tracker
# ==================================================

import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 190.00,
    "NVDA": 120.00,
    "META": 500.00
}


def display_available_stocks():
    print("\nAvailable Stocks")
    print("-" * 35)
    print(f"{'Stock Symbol':<15}{'Price ($)':>12}")
    print("-" * 35)

    for stock, price in stock_prices.items():
        print(f"{stock:<15}{price:>12.2f}")

    print("-" * 35)


def calculate_portfolio():
    portfolio = []

    print("=" * 50)
    print("          STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    display_available_stocks()

    while True:
        stock = input(
            "\nEnter stock symbol (or DONE to finish): "
        ).strip().upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Invalid stock symbol. Please try again.")
            continue

        try:
            quantity = int(
                input(f"Enter quantity of {stock}: ")
            )

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print("Invalid quantity. Enter a positive whole number.")
            continue

        price = stock_prices[stock]

        try:
            investment = price * quantity
        except OverflowError:
            print("Quantity is too large to calculate. Please try a smaller number.")
            continue

        portfolio.append({
            "Stock": stock,
            "Quantity": quantity,
            "Price": price,
            "Investment": investment
        })

        print(f"{stock} added successfully!")
        print(f"Investment value: ${investment:.2f}")

    if not portfolio:
        print("\nNo stocks were added to the portfolio.")
        print("Thank you for using Stock Portfolio Tracker!")
        return

    # Calculate total investment
    total_investment = sum(
        item["Investment"] for item in portfolio
    )

    # Display portfolio summary
    print("\n" + "=" * 65)
    print("                 PORTFOLIO SUMMARY")
    print("=" * 65)

    print(
        f"{'Stock':<12}"
        f"{'Quantity':<12}"
        f"{'Price ($)':<15}"
        f"{'Investment ($)':<18}"
    )

    print("-" * 65)

    for item in portfolio:
        print(
            f"{item['Stock']:<12}"
            f"{item['Quantity']:<12}"
            f"{item['Price']:<15.2f}"
            f"{item['Investment']:<18.2f}"
        )

    print("-" * 65)
    print(f"TOTAL INVESTMENT: ${total_investment:.2f}")
    print("=" * 65)

    # Optional CSV file handling
    save_choice = input(
        "\nSave portfolio to CSV file? (yes/no): "
    ).strip().lower()

    if save_choice in ("yes", "y"):
        filename = "stock_portfolio.csv"

        try:
            with open(
                filename,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                fieldnames = [
                    "Stock",
                    "Quantity",
                    "Price",
                    "Investment"
                ]

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(portfolio)

                writer.writerow({
                    "Stock": "TOTAL",
                    "Quantity": "",
                    "Price": "",
                    "Investment": f"{total_investment:.2f}"
                })

            print(
                f"Portfolio saved successfully to {filename}!"
            )

        except OSError as error:
            print(f"Unable to save file: {error}")

    print("\nThank you for using Stock Portfolio Tracker!")


# Main program
if __name__ == "__main__":
    try:
        calculate_portfolio()
    except EOFError:
        print("\nInput ended. Exiting Stock Portfolio Tracker.")
