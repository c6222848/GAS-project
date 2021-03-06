from Queue_rij import Queue
import sys
from Bestelling import *
from adttabel import *
from stock import *
from functools import reduce
from gebruiker import *
from werknemer_modified import *

class Chocolademelk:
    prijs=0
    id=0
    credit=0
    bruin=0
    wit=0
    zwart=0
    melk=0
    chilipeper=0
    honing=0
    marshmallow=0

    def __init__(self,zwart=0,wit=0,bruin=0,melk=0,chilipeper=0,honing=0,marshmallow=0):
        self.zwart=zwart
        self.wit=wit
        self.melk=melk
        self.bruin=bruin
        self.chilipeper=chilipeper
        self.honing=honing
        self.marshmallow=marshmallow
        self.prijs=2+zwart*1+wit*1+bruin*1+melk*1+marshmallow*0.75+chilipeper*0.25+honing*0.5

    def addingredient(self,ingredient):
        if ingredient=="chilipeper":
            self.chilipeper+=1
            self.prijs+=Chilipeper.price
        elif ingredient=="marshmallow":
            self.marshmallow+=1
            self.prijs+=Marshmallow.price
        elif ingredient=="honing":
            self.honing+=1
            self.prijs+=Honing.price
        elif ingredient=="wit":
            self.wit+=1
            self.prijs+=ChocoladeShot.price
        elif ingredient=="bruin":
            self.bruin+=1
            self.prijs+=ChocoladeShot.price
        elif ingredient=="melk":
            self.melk+=1
            self.prijs+=ChocoladeShot.price
        elif ingredient=="zwart":
            self.zwart+=1
            self.prijs+=ChocoladeShot.price

    def berekenworkload(self):
        return 5+self.bruin+self.wit+self.melk+self.marshmallow+self.honing+self.zwart+self.chilipeper


def str_to_class(str):#code from https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object, credit to sixthgear
    return reduce(getattr, str.split("."), sys.modules[__name__])

class Winkel:
    allewerknemers=Tabel()
    werknemerbeschikbaar=Stack()
    werknemersaantwerken=Tabel()
    bestellingenwaiting=Queue()
    bestellingenfinished=Tabel()
    nieuwbestellingen=Queue()
    gebruikers=Tabel()


    def __init__(self):
        self.werknemerbeschikbaar=Stack()
        self.werknemers=Tabel()
        self.bestellingen=Queue()

    def update(self):

        templist = self.werknemersaantwerken.traverse()
        for i in templist:
            i.werken()
            if i.bestelling.afgehaald==True:
                self.werknemerbeschikbaar.push(i)
                self.werknemersaantwerken.remove(i.id)
                self.bestellingenfinished.insert(i.bestelling.timestamp,i.bestelling)
                i.bestellingdone()#veranderen de bestelling van de werknemer terug naar None
        if self.bestellingenwaiting.isempty()==False and self.werknemerbeschikbaar.isEmpty()==False:
            self.werknemerbeschikbaar.getTop().bestellingenaannemen(self.bestellingenwaiting.gettop())
            self.werknemersaantwerken.insert(self.werknemerbeschikbaar.getTop().id,self.werknemerbeschikbaar.getTop())
            self.werknemerbeschikbaar.pop()

        self.nieuwbestellingen=Queue() #reset de nieuwe bestelling na elke tijdstip


    def addbestelling(self,bestelling):
        self.bestellingenwaiting.insert(bestelling)
        self.nieuwbestellingen.insert(bestelling)#dit is nodig bij log

    def addgebruiker(self,gebruiker):
        self.gebruikers.insert(gebruiker.email,gebruiker)

    def addwerknemers(self,werknemer):
        werknemer.id=self.allewerknemers.size()
        self.allewerknemers.insert(werknemer.id,werknemer)
        self.werknemerbeschikbaar.push(werknemer)



def initfunction(line,stock,winkel):
    availablechoises={"shot","honing","chilipeper","gebruiker","marshmallow","werknemer"}
    availableshots = {"wit","zwart","bruin","melk"}
    seperatedline = line.split(" ")
    if seperatedline[0] not in availablechoises:
        print("check typfout in de lijn: ",line)
        return False
    else:
        if seperatedline[0]=="shot" and len(seperatedline)==6:
            if seperatedline[1] not in availableshots:
                print("check parameter in de lijn: ", line)
                return False
            else:
                counter=int(seperatedline[2])
                for i in range(counter):
                    soort=seperatedline[1]
                    temp=str_to_class("ChocoladeShot")(soort,seperatedline[3],seperatedline[4],seperatedline[5])#345 is jaar maand dag
                    stock.addStock(temp)
        elif len(seperatedline)==5 and seperatedline[0] not in {"shot","gebruiker","werknemer"}:
            counter=int(seperatedline[1])
            for i in range(counter):
                temp=str_to_class(seperatedline[0].capitalize())(seperatedline[2],seperatedline[3],seperatedline[4])
                stock.addStock(temp)
        elif seperatedline[0] in{"gebruiker","werknemer" }and len(seperatedline)==4:
            voornaam=seperatedline[1]
            achternaam=seperatedline[2]
            workloadofemailadress=seperatedline[3]
            if seperatedline[0]=="gebruiker":
                temp = str_to_class(seperatedline[0].capitalize())(voornaam, achternaam, workloadofemailadress)
                winkel.addgebruiker(temp)
            else:
                temp = str_to_class(seperatedline[0].capitalize())(voornaam, achternaam, int(workloadofemailadress))
                winkel.addwerknemers(temp)
            #voor gebruiker is 3 de emailadress en voor werknemer is 3 de workload
        else:
            print("check parameter in de lijn: ", line)
            return False



def startingfunction(line,stock,winkel,time):
    seperatedline = line.split(" ")
    availablechoises={"bestel","stock","log"}
    if seperatedline[1] not in availablechoises:
        print("check line:",line)
        return False
    if seperatedline[0].isdigit()==False:
        print("check timestamp, it's wrong on line:", line)
        return False
    while int(seperatedline[0])>time:
        winkel.update()
        time+=1
    else:
        if seperatedline[1]=="bestel":
            chocolademelk=Chocolademelk()
            emailadress=seperatedline[2]
            bestelling=Bestelling(emailadress,time)
            for i in range(3,len(seperatedline)):#this needs to change, possibly
                chocolademelk.addingredient(seperatedline[i])
            winkel.addbestelling(bestelling)
        elif seperatedline[1]=="stock":
            linepreparedforinit=line[7:]+" unknown"+" unknown"+" unknown"
            initfunction(linepreparedforinit,stock,winkel)
        elif seperatedline[1]=="log":
            pass







if __name__ =="__main__":
    input=open("input.txt","r")
    initing=False
    starting=False
    stock=Stock()
    winkel=Winkel()
    counter=0
    for line in input:
        line=line.strip('\n')
        if line[:5]=="chili":
            line="chilipeper"+line[5:]
        print(line)

        if line=="init":
            initing=True
            starting=False
            continue
        elif line=="start":
            starting=True
            initing=False
            continue
        if initing:
            if initfunction(line,stock,winkel)==False:
                break
        if starting:
            if startingfunction(line,stock,winkel,counter)==False:
                break
            counter=int(line[0])
        #print(line)
