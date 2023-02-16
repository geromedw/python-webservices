import requests
import random
from datetime import datetime
import json

class api:
    def __init__(self) -> None:
        pass

    def opvragen(self):
        antwoord = requests.get("https://spyapi.admkrm.repl.co/boodschappen")
        return antwoord.text
    
    def posten(self,titel,boodschap,zender,ontvanger,groep):
        randomgetal = random.randint(0,5000)
        now = datetime.now()
        test = requests.post(f"https://spyapi.admkrm.repl.co/boodschappen",json={'titel': titel, 'boodschap': self.incodeeerboodschap(randomgetal,boodschap), 'datum': now.isoformat() , 'zender':zender, 'ontvanger': ontvanger, 'groep':groep,'id': randomgetal})
        print(test.text)
        print(randomgetal)

    def verwijderen(self,id):
        requests.delete(f"https://spyapi.admkrm.repl.co/boodschappen/{id}")

    def boodschap(self,id):
        waarde = self.jsonparser(id) 
        try : 
            boodschap = self.decodeboodschap(id,waarde["boodschap"])
            return boodschap
        except:
            boodschap = requests.get(f'https://spyapi.admkrm.repl.co/boodschappen/{id}')
            return boodschap.text
        

    
    def groep(self,groepsnaam):
        groepsbrichten = requests.get(f'https://spyapi.admkrm.repl.co/boodschappen/groep/{groepsnaam}')
        return groepsbrichten.text
    
    def boodschapaanpassen(self,id,boodschap):
        jsonresponse = self.jsonparser(id)
        requests.put(f'https://spyapi.admkrm.repl.co/boodschappen/{id}',json={'titel': jsonresponse["titel"], 'boodschap': self.incodeeerboodschap(id,boodschap), 'datum': datetime.now().isoformat() , 'zender':jsonresponse["zender"], 'ontvanger': jsonresponse["ontvanger"], 'groep':jsonresponse["groep"],'id': jsonresponse["id"]})
        return self.boodschap(id)
    
    def jsonparser(self,id):
        response = requests.get(f'https://spyapi.admkrm.repl.co/boodschappen/{id}')
        return response.json()
    
    def incodeeerboodschap(self,id,boodschap):
        incrementwoord = {}
        woorden = boodschap.split()
        for woord in range(len(woorden)):
            incrementwoord.update({woord:[]})
            for letter in range(len(woorden[woord])):
                incrementwoord[woord].append(ord(woorden[woord][letter])*id)
        return json.dumps(incrementwoord)

    def decodeboodschap(self,id,boodschap):
        boodschap = json.loads(boodschap)
        decodeboodschap = ""
        for key in boodschap:
            for value in boodschap[key]:
                decodeboodschap += chr(int(value/id))
            decodeboodschap += " "
        return(decodeboodschap)
            
API = api()

print("wat wilt u doen? \n 1. alle berichten inlezen. \n 2. lees geincrepteerde boodschap in. \n 3. alle berichten van een groep inlezen \n 4. een boodschap maken \n 5. een boodschap aanpassen \n 6. een boodschap verwijderen")
keuze=int(input())
if keuze == 1:
    print(API.opvragen())
if keuze == 2:
    id = int(input("geef een id op"))
    print(API.boodschap(id))
if keuze == 3:
    groep=input("geef de groepsnaam op")
    API.groep(groep)
if keuze == 4:
    titel = input("geef een titel op")
    boodschap = input("geef een boodschap op")
    zender = input("geef de zender op")
    ontvanger = input("geef de ontvanger op")
    groep = input("geef een groep op")
    API.posten(titel,boodschap,zender,ontvanger,groep) 
if keuze == 5:
    id = int(input("geef een id op"))
    boodschap = input("geef de nieuwe boodschap op")
    API.boodschapaanpassen(id,boodschap)
if keuze == 6:
    id = int(input("geef een id op"))
    API.verwijderen(id)

#print(API.opvragen().text)
#API.posten("kasei", "de zon staat op 90 graden","wandelaar","weerspecialist","weerraportering")
#print(API.boodschap(2126))
#print(API.groep("raketlancering"))
#print(API.boodschapaanpassen(2126,"de aarde staat op 4 graden"))
#print(API.boodschap(2126))
#codeboodschap = API.incodeeerboodschap(20,"hallo dit is een test")
#API.decodeboodschap(20,codeboodschap)