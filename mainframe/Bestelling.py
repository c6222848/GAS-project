from stock import *

class Bestelling:
    def __init__(self,gebruikersid,timestamp): #bestelling.
        self.gebruikersid = gebruikersid #contains id
        self.timestamp = timestamp #timestamp
        self.aantalshots = []
        #i didn't really use the aantal shot, it will be a lot more harder if i user it.
        self.extraIngredient = []
        self.afgehaald = False
        self.prijs=2
        self.credits = 5 # in credits
    def Afgehaald(self):
        self.afgehaald = True

    def VoegIngredientToe(self,Ingredient):
        self.extraIngredient.append(Ingredient)
        if Ingredient in ["Wit","Zwart","Bruin","Melk"]:
            self.prijs+=ChocoladeShot.price
        else:
            self.prijs+=str_to_class(Ingredient).price
        self.credits += 1

    def printBestelling(self):
        #beacause it's all string form, this is way easier to print.
        print("Ingredienten")
        for i in self.extraIngredient:
            print(i,",",end="")
            print()