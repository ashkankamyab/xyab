#!/usr/bin/env python3
import locale
import requests
import sys
import json
from collections import defaultdict

# Intial setup and global variables
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:10.0.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
api = 'https://api.tgju.online/v1/data/sana/json'

# Currencies Container
currency = defaultdict(lambda: "Not Present")


currency = defaultdict(lambda: "Not Present")
def update_data():
    data = requests.get(api, headers=headers).text
    data = json.loads(data)
    for element in data["sana"]["data"]:
        currency[element["slug"]] = element
    return currency


# The Rate Graber function
def rate_graber(input='sana_buy_eur'):
    curency = update_data()
    date = curency[input]["t"]
    title = curency[input]["title"]
    rate = locale.currency(curency[input]["p"]/10, grouping=True, symbol=False)
    return("{}:  {} تومان\n\n{}".format(title, rate, date))


if __name__ == "__main__":
    print(rate_graber())