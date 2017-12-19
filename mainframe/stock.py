from doubleketting import *
import sys
from functools import reduce

def str_to_class(str):#code from https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object, credit to sixthgear and more.
    return reduce(getattr, str.split("."), sys.modules[__name__])


class tabel:
    content=dict()

    def __init__(self):
        self.content=dict()

    def add(self,key,val):
        self.content[key]=val

    def remove(self,key):
        self.content.pop(key)

    def retrieve(self,key):
        return self.content.get(key,None)

    def size(self):
        return len(self.content)

    def isempty(self):
        return len(self.content)==0

class Stock(tabel):
    def __init__(self):
        tabel.__init__(self)
        self.content["chilipeper"] = doubleketting()
        self.content["honing"] = doubleketting()
        self.content["marshmallow"] = doubleketting()
        #self.content["chocoladeshot"] = doubleketting()
        #I kinda need this change to make it easier for me and for my team.
        self.content["melk"] = doubleketting()
        self.content["wit"] = doubleketting()
        self.content["zwart"] = doubleketting()
        self.content["bruin"] = doubleketting()

    def addStock(self, item):
        #this gets a class object, and we need to call str to class to get the class.. i guess? and once we know what kind of item it is, just insert it into the right chain.
        if type(item) == str_to_class("Marshmallow"):
            self.content["marshmallow"].insert(item)
        elif type(item) == str_to_class("ChocoladeShot"):
            if item.soort=="wit":
                self.content["wit"].insert(item)
            elif item.soort=="melk":
                self.content["melk"].insert(item)
            elif item.soort=="zwart":
                self.content["zwart"].insert(item)
            elif item.soort=="bruin":
                self.content["bruin"].insert(item)
        elif type(item) == str_to_class("Chilipeper"):
            self.content["chilipeper"].insert(item)
        elif type(item) == str_to_class("Honing"):
            self.content["honing"].insert(item)
        return True

    def deleteStock(self, item):
        #same thing, but now we're getting a string, and it's lot more easier.
        if item == "marshmallow":
            self.content["marshmallow"].delete()
        elif item == "wit":
            self.content["wit"].delete()
        elif item == "melk":
            self.content["melk"].delete()
        elif item == "zwart":
            self.content["zwart"].delete()
        elif item == "bruin":
            self.content["bruin"].delete()
        elif item == "chili":
            self.content["chilipeper"].delete()
        elif item == "honing":
            self.content["honing"].delete()
        return True

    #sort methode : producten met vroegst vervaldatum komt eerst
    def sort(self):#oh.. well.. i guess it's in the final version then.
        pass


#from here on it's just the class of all the ingredients, with a fixed price and init function which inits the expiry date.
class Chilipeper(tabel):
    price = 0.25
    def __init__(self, expiryDate,yy,mm):
        tabel.__init__(self)
        self.expiryDate = expiryDate

class Honing(tabel):
    price = 0.5
    def __init__(self, expiryDate,yy,mm):
        tabel.__init__(self)
        self.expiryDate = expiryDate

class Marshmallow(tabel):
    price = 0.75
    def __init__(self, expiryDate,yy,mm):
        tabel.__init__(self)
        self.expiryDate = expiryDate

class ChocoladeShot(tabel):
    price = 1.0

    def __init__(self,soort, expiryDate,yy,mm):
        tabel.__init__(self)
        self.expiryDate = expiryDate
        self.soort = soort