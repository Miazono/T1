# Import necessary libraries and modules
import flask 
import requests

import requests
import json
from flask import Flask

# Function to retrieve a list of currency values from Central Bank of Russia's daily JSON
def get_currencies_list():
    """
     Fetch and return a list of currencies from CBR XML;

     This function sends GET request to get JSON format data about currencies, 
     then extract values of each currency into list and then returns list.
     
     Returns:
         list: A list containing the currencies values from the API response.
    """
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    currencies = list(data['Valute'].values())
    return currencies

# Create Flask web-application 
app = Flask(__name__)


def create_html(currencies):
    """
    Create HTML content to display recieved list if currencies.

    This function creates an HTML table with currencies data.

    Returns:
        string: A string containing the generated HTML content.
    """
    DISPLAYED_ATTRS = {"CharCod", "Name", "Value", "Previous"}
    text = '<h1>Курс валют</h1>'
    text += '<table>'
    text += '<tr>'
    for _ in currencies[0]:
        text += f'<th><th>'
    text += '</tr>'
    for currency in currencies:
        text += '<tr>'
        for attr in DISPLAYED_ATTRS:
            text += f'<td>{currency.get(attr, "")}</td>'
        text += '</tr>'

    text += '</table>'
    return text

# Define the route for the root of the URL
@app.route("/")
def index():
    """
    Handle request to the root URL.

    Function fetches CBR data with function get_currencies_list() to form HTML content with create_html(currencies)
    and finally display it by return of the generated text.
    
    Returns:
        string: A string containing the generated HTML content.
    """
    currencies = get_currencies_list()
    html = create_html(currencies)
    return html


if __name__ == "__main__":
    app.run()