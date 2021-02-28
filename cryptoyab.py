#!/usr/bin/env python3

from pycoingecko import CoinGeckoAPI
from datetime import date

"""
API: https://www.coingecko.com/en/api#explore-api
"""


cg = CoinGeckoAPI()

def get_crypto_price(crypto_currency='bitcoin', vs_currency='usd', novolume=True):
    if novolume:
        return(cg.get_price(ids=crypto_currency, vs_currencies=vs_currency))

    # Reutrn
    else:
        return (""" 
        This feature is not supported yet,
        And will be released within the next fewer versions.
        """
        )

def euro_based_price(crypto_currency='bitcoin', vs_currency='eur', novolume=True):
    if novolume:
        #FIXME: calling vs_currency in return can harme the code
        priceList = (cg.get_price(ids=crypto_currency, vs_currencies=vs_currency))
        today = date.today()
        today = today.strftime("%B %d %Y")
        for k,v in priceList.items():
            return("{},  {}: {}".format(today, k, v['eur']))

if __name__ == "__main__":
    print(get_crypto_price(['bitcoin', 'litecoin', 'ethereum'], ['usd', 'eur']))
