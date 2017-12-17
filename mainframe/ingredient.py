from adttabel import *
from datetime import date

class Chilipeper(Tabel):
    def __init__(self, expiryDate, amount):
        Tabel.__init__(self)
        self.expiryDate = expiryDate
        self.amount = amount


    def wijzigingchilipeper(self, expiryDate, amount):
        if expiryDate == self.expiryDate:
            self.insert(expiryDate, amount)
            return True
        return False

    def destroyChilipeper(self, expiryDate):
        if expiryDate == self.expiryDate:
            self.remove(expiryDate)
            return True
        return False

    #def dest(self):
     #   today = date.today()
      #  if today == self.expiryDate:
       #     self.remove(today)
        #    return True
        #return False

    def getlength(self):
        return self.size()

    def find(self,expiryDate):
        if expiryDate == self.expiryDate:
            print(self.retrieve(expiryDate))
            return True
        return False

class Honing(Tabel):
    def __init__(self, expiryDate, amount):
        Tabel.__init__(self)
        self.expiryDate = expiryDate
        self.amount = amount

    def wijzigingHoning(self, expiryDate, amount):
        if expiryDate == self.expiryDate:
            self.insert(expiryDate, amount)
            return True
        return False

    def destroyHoning(self, expiryDate):
        if expiryDate == self.expiryDate:
            self.remove(expiryDate)
            return True
        return False

    def getlength(self):
        return self.size()

    def find(self, expiryDate):
        if expiryDate == self.expiryDate:
            print(self.retrieve(expiryDate))
            return True
        return False

class Marshmallow(Tabel):
    def __init__(self, expiryDate, amount):
        Tabel.__init__(self)
        self.expiryDate = expiryDate
        self.amount = amount

    def wijzigingMarshmallow(self, expiryDate, amount):
        if expiryDate == self.expiryDate:
            self.insert(expiryDate, amount)
            return True
        return False

    def destroyMarshmallow(self, expiryDate):
        if expiryDate == self.expiryDate:
            self.remove(expiryDate)
            return True
        return False

    def getlength(self):
        return self.size()

    def find(self, expiryDate):
        if expiryDate == self.expiryDate:
            print(self.retrieve(expiryDate))
            return True
        return False

class ChocoladeShot(Tabel):
    def __init__(self, expiryDate, amount):
        Tabel.__init__(self)
        self.expiryDate = expiryDate
        self.amount = amount

    def wijzigingChocoladeShot(self, expiryDate, amount):
        if expiryDate == self.expiryDate:
            self.insert(expiryDate, amount)
            return True
        return False

    def destroyChocoladeShot(self, expiryDate):
        if expiryDate == self.expiryDate:
            self.remove(expiryDate)
            return True
        return False

    def getlength(self):
        return self.size()

    def find(self, expiryDate):
        if expiryDate == self.expiryDate:
            print(self.retrieve(expiryDate))
            return True
        return False

#a = chilipeper("2017-12-16", 50)
a = chilipeper(2017,50)
a.getlength()
a.find(2017)