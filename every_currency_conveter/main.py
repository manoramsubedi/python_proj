from requests import get 
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = ""

printer = PrettyPrinter() #provide format for json

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    printer.pprint(data)

get_currencies()



