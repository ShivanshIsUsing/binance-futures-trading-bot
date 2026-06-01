from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        if order_type.upper() == "LIMIT":

            if price is None:
                raise ValueError("Price required for LIMIT order")

            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"ORDER REQUEST => {params}")

        response = client.futures_create_order(**params)

        logger.info(f"ORDER RESPONSE => {response}")

        return response

    except Exception as e:

        logger.error(f"ORDER FAILED => {str(e)}")
        raise