import requests
import random
import json
class Quote():

    def swanson(self):
        returnMe = random.randint(0,4)
        if returnMe == 0:
            resp = requests.get('https://ron-swanson-quotes.herokuapp.com/v2/quotes')
            if resp.status_code != 200:
                return 'I could not get my Swanson quote'
            else:
                myQuote = resp.json()
                myQuoteString = myQuote[0]
                return myQuoteString + " -- Ron Swanson"
        elif returnMe == 1:
            resp = requests.get('https://zenquotes.io/api/today')
            if resp.status_code != 200:
                return 'I could not find a quote of the day'
            else:
                myQuote = resp.json()
                myQuoteString = myQuote[0]
                return myQuoteString["q"] + " -- " + myQuoteString["a"]

        elif returnMe == 2:
            return "Luke has a hairy butt"
        elif returnMe == 3:
            return "Finn is afraid of Fairies"
        else:
            return "Keely and Stony have smelly feet"