import requests
import random
import json

class Quote(object):
    def swanson(self):
        try:
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
                    return 'I could not find a quote of the day/n Zenquotes did not respond'
                else:
                    myQuote = resp.json()
                    myQuoteString = myQuote[0]
                    return myQuoteString["q"] + " -- " + myQuoteString["a"]
            else:
                staticQuotes = ["Luke has a hairy butt",
                    "Finn is afraid of Fairies",
                    "Keely and Stony have smelly feet"]
                qNum = random.randint(0, len(staticQuotes))
                return staticQuotes[qNum]
        except Exception as e:
            message = f'Could not get a quote\n {e}'
            return message
