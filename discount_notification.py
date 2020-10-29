from twilio.rest import Client
import time
from os import getenv
from amazon_price import get_price


def catalizer(price):
    #TODO: Compehrhention Loop
    catalized = ""
    for char in price:
        if char not in ["$", "€", "."]:
            catalized += char
    
    digitized = ".".join(catalized.split(","))
    return float(digitized)


def check_price(URL, wish_price):
    history = (get_price(URL))
    price = catalizer(history[0])

    if not isinstance(wish_price, int) or isinstance(wish_price, float):
        raise TypeError('Desired Price should be Int or Double decimal')
 
    if(price):
        Client(getenv('ACCOUNT_SID'), getenv('AUTH_TOKEN')).messages.create(
                from_='whatsapp:+14155238886', # In What's app this is fix
                body=price,
                to='whatsapp:+491715169514'
        )
    # TODO:
    # elif:
    # else:
if __name__ == "__main__":
    while True:
        check_price(200, getenv("AMAZON_URL"))
        time.sleep((60 * 60) * 6)

