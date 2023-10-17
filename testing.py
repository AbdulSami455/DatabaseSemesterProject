

import requests
from requests.exceptions import ConnectionError
import time
API_KEY="WQW9CPLA6FXJPS55"

#Daily Stats about stocks
def Daily_Data(API_KEY):
#Intraday Stock Prices
 url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={API_KEY}"


#To Establish Connections _Use of Retries and Delay
 max_retries = 3
 retry_delay = 5  # in seconds

 for _ in range(max_retries):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Check for HTTP status code errors
        data=r.json()
        print(data)
        break  # If successful, exit the loop
    except ConnectionError:
        print("ConnectionError. Retrying in {} seconds...".format(retry_delay))
        time.sleep(retry_delay)
 else:
    print("Max retries exceeded. Unable to establish a connection.")

#Intraday Stock Prices
def Intraday(API_KEY):

 url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={API_KEY}"


#To Establish Connections _Use of Retries and Delay
 max_retries = 3
 retry_delay = 5  # in seconds

 for _ in range(max_retries):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Check for HTTP status code errors
        data=r.json()
        print(data["Global Quote"]["05. price"])
        break  # If successful, exit the loop
    except ConnectionError:
        print("ConnectionError. Retrying in {} seconds...".format(retry_delay))
        time.sleep(retry_delay)
 else:
    print("Max retries exceeded. Unable to establish a connection.")


def companyoverview(API_KEY):
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey={API_KEY}"

    # To Establish Connections _Use of Retries and Delay
    max_retries = 3
    retry_delay = 5  # in seconds

    for _ in range(max_retries):
        try:
            r = requests.get(url)
            r.raise_for_status()  # Check for HTTP status code errors
            data = r.json()
            print(data)
            break  # If successful, exit the loop
        except ConnectionError:
            print("ConnectionError. Retrying in {} seconds...".format(retry_delay))
            time.sleep(retry_delay)
    else:
        print("Max retries exceeded. Unable to establish a connection.")


def monthlydata(API_KEY):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey={API_KEY}"

    # To Establish Connections _Use of Retries and Delay
    max_retries = 3
    retry_delay = 5  # in seconds

    for _ in range(max_retries):
        try:
            r = requests.get(url)
            r.raise_for_status()  # Check for HTTP status code errors
            data = r.json()
            print(data)
            break  # If successful, exit the loop
        except ConnectionError:
            print("ConnectionError. Retrying in {} seconds...".format(retry_delay))
            time.sleep(retry_delay)
    else:
        print("Max retries exceeded. Unable to establish a connection.")
#Intraday(API_KEY)
companyoverview(API_KEY)
#monthlydata(API_KEY)