#!/usr/bin/env python3
import requests

import bs4
from sys import argv


"""
Scrapper: get_price() digs amazon URL and exracts the ProductID of it.
Product ID is the very most unique part of amazon store.
This helps to use the online portal camelcamelcamel.com.
This approache makes this script persistence.
"""


def get_price(URL):
    country_prefix = ""
    if "amazon.de" in URL:
        country_prefix = "de."
        URL = URL.replace("/dp/", "/product/")

    URL = URL.replace("?", "/")
    ProductID = URL.split("/product/", 1)[1].split("/")[0]

    headers = {
        'authority': 'www.camelcamelcamel.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Chrome x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    htmldata = requests.get("https://" + country_prefix + "camelcamelcamel.com/product/" + ProductID, headers=headers)
    soup = bs4.BeautifulSoup(htmldata.text, 'html.parser')

    current = soup.find("span", {'class': 'green'}).text
    try:
        lowest = soup.find("tr", {'class': 'lowest_price'}).text.strip().split("\n")[1:]
        highest = soup.find("tr", {'class': 'highest_price'}).text.strip().split("\n")[1:]
        return([current, lowest, highest])
    except AttributeError:
        return(current)

       
    '''
    This could be handy for futur advance comparison or maybe auto order.
    highest  = ".".join(soup.find("tr", {'class': 'highest_price'}).text.strip().split("\n")[1][:-1].split(","))
    lowest = ".".join(soup.find("tr", {'class': 'lowest_price'}).text.strip().split("\n")[1][:-1].split(","))
    '''
    





if __name__ == "__main__":
    if len(argv) == 2:
        print(get_price(argv[1]))
    else:
        print("usage: {} URL".format(argv[0]))
        print("e.g {} https://www.amazon.de/dp/B076V3VB6N/".format(argv[0]))