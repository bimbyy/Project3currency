from flask import Flask, render_template, request
import requests

currency_symbols = {
    "AED": "د.إ",  # United Arab Emirates Dirham
    "AUD": "$",    # Australian Dollar
    "BRL": "R$",   # Brazilian Real
    "CAD": "$",    # Canadian Dollar
    "CHF": "Fr",   # Swiss Franc
    "CNY": "¥",    # Chinese Yuan
    "EUR": "€",    # Euro
    "GBP": "£",    # British Pound Sterling
    "HKD": "$",    # Hong Kong Dollar
    "INR": "₹",    # Indian Rupee
    "JPY": "¥",    # Japanese Yen
    "KRW": "₩",    # South Korean Won
    "MXN": "$",    # Mexican Peso
    "NZD": "$",    # New Zealand Dollar
    "RUB": "₽",    # Russian Ruble
    "SGD": "$",    # Singapore Dollar
    "TRY": "₺",    # Turkish Lira
    "USD": "$",    # United States Dollar
    "ZAR": "R",    # South African Rand
}
# Function to fetch exchange rate
def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate.host/latest"
    params = {
        "base": from_currency,
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "rates" in data:
        rates = data["rates"]
        if to_currency in rates:
            exchange_rate = rates[to_currency]
            return exchange_rate
        else:
            return None
    else:
        return None

# Function to fetch the list of supported currency codes from the API
def get_supported_currency_codes():
    url = "https://api.exchangerate.host/latest"
    response = requests.get(url)
    data = response.json()
    return list(data["rates"].keys())

# Function to fetch currency symbols from the API
def get_currency_symbols():
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()
    
    currency_symbols = {}
    for currency_code, currency_data in data.get('symbols', {}).items():
        currency_symbols[currency_code] = currency_data.get('symbol', '')
    
    return currency_symbols

# Function to perform currency conversion
def convert_currency(from_currency, to_currency, amount):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    currency_symbols = get_currency_symbols()  # Retrieve currency symbols
    
    if exchange_rate is not None:
        converted_amount = round(amount * exchange_rate, 2)
        to_currency_symbol = currency_symbols.get(to_currency, "")
        return converted_amount, to_currency_symbol
    else:
        return None, ""

@app.route("/", methods=["GET", "POST"])
def currency_converter():
    #initializing result_amount and result_symbol
    result_amount = None
    result_symbol = ""
    #checking post
    if request.method == "POST":
        #getting data from post
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        amount = request.form["amount"]
        #grabbing list of supported currency codes
        supported_currency_codes = get_supported_currency_codes()
        #checking if currency codes are valid
        if (
            from_currency in supported_currency_codes
            and to_currency in supported_currency_codes
        ):
            #attempting to conver enterend amount
            try:
                amount = float(amount)
                #calling function to conver the currency
                converted_amount, result_symbol = convert_currency(from_currency, to_currency, amount)
                #if failed return an error
                if converted_amount is not None:
                    return render_template("converter.html", result_amount=converted_amount, result_currency_symbol=result_symbol)
                else:
                    return "Unable to retrieve exchange rate data."

            except ValueError:
                return "Invalid amount. Please enter a valid number."
        else:
            return "Invalid currency codes. Please enter valid currency codes."
    #Just render the inital page with default values
    return render_template("converter.html", result_amount=result_amount, result_currency_symbol=result_symbol)
#start the flask application
if __name__ == "__main__":
    app.run(debug=True)
