import requests
import random
import datetime

class api:
    def __init__(self) -> None:
        pass

    def opvragen(self):
        antwoord = requests.get("https://spyapi.admkrm.repl.co/boodschappen")
        return antwoord
    
    def posten(self,titel,boodschap,zender,ontvanger,groep):
        randomgetal = random.randint(0,5000)
        test = requests.put(f"https://spyapi.admkrm.repl.co/boodschappen/{randomgetal}",json='{"titel": titel, "boodschap": boodschap, "datum": datetime.datetime.now, "zender":zender, "ontvanger": ontvanger, "groep":groep,"id": randomgetal}')
        print(test.text)


API = api()

print(API.opvragen().text)
API.posten("Virus","U computer heeft een virus", "Microsoft", "Boma","The Vanguard Group")