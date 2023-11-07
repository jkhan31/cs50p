import json
import sys
import requests

def main():
    # check for command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # check if command-line argument is a number
    usd = get_number()

    # Query API for CoinDesk Bitcoin Price Index USD rate
    rate = get_rate()

    # convert
    amt = usd * rate
    print(f"${amt:,.4f}")


def get_number():
    # check if command-line argument is a number
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

def get_rate():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        # Return USD rate as float
        return o["bpi"]["USD"]["rate_float"]
    except ValueError:
        pass


if __name__ == "__main__":
    main()