#!/usr/bin/env python3

from pycoingecko import CoinGeckoAPI

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


if __name__ == "__main__":
    print(get_crypto_price(['bitcoin', 'litecoin', 'ethereum'], ['usd', 'eur']))
