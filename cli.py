import argparse

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)


def interactive_mode():

    print("\n==========================")
    print(" Binance Trading Bot ")
    print("==========================\n")

    symbol = input("Enter Symbol (e.g. BTCUSDT): ").strip()

    while True:
        side = input("Enter Side (BUY/SELL): ").strip().upper()

        if side in ["BUY", "SELL"]:
            break

        print("❌ Invalid side. Choose BUY or SELL.")

    while True:
        order_type = input(
            "Enter Order Type (MARKET/LIMIT): "
        ).strip().upper()

        if order_type in ["MARKET", "LIMIT"]:
            break

        print("❌ Invalid order type.")

    while True:
        try:
            quantity = float(
                input("Enter Quantity: ")
            )

            if quantity > 0:
                break

            print("❌ Quantity must be positive.")

        except ValueError:
            print("❌ Enter a valid number.")

    price = None

    if order_type == "LIMIT":

        while True:
            try:
                price = float(
                    input("Enter Price: ")
                )
                break

            except ValueError:
                print("❌ Enter a valid price.")

    return {
        "symbol": symbol,
        "side": side,
        "order_type": order_type,
        "quantity": quantity,
        "price": price
    }


def command_line_mode():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Bot"
    )

    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--quantity")
    parser.add_argument("--price")

    return parser.parse_args()


def main():

    print("\nChoose Mode:")
    print("1. Interactive Menu")
    print("2. Command Line Arguments")

    choice = input("\nSelect option (1 or 2): ")

    if choice == "1":

        data = interactive_mode()

        response = place_order(
            symbol=data["symbol"],
            side=data["side"],
            order_type=data["order_type"],
            quantity=data["quantity"],
            price=data["price"]
        )

    else:

        args = command_line_mode()

        if not all([
            args.symbol,
            args.side,
            args.type,
            args.quantity
        ]):
            print(
                "\n❌ Missing command line arguments.\n"
                "Example:\n"
                "python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001"
            )
            return

        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        response = place_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=args.price
        )

    print("\n==========")
    print("ORDER RESPONSE")
    print("==========")

    print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Qty: {response.get('executedQty')}")
    print(f"Average Price: {response.get('avgPrice', 'N/A')}")

    print("\n✅ SUCCESS")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ ERROR: {e}")