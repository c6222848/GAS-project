class ItemValue:
    def __init__(self, data, item):
        self.data = data
        self.item = item
class Node:
    def __init__(self):
        self.numOfItems = 0
        self.parent = None
        self.arrayChild = [] #array van knopen
        self.arrayItem = [] #array van data items in een knoop
        #Array initialiseren
        for i in range(4):
            self.arrayChild.append(None)
        for j in range(3):
            self.arrayItem.append(None)

    # vind data item in een knoop
    def retrieveItem(self, key):
        #als niets in pos i sta dan hoef je niet verder te kijken, doe break, item niet gevonden
        for i in range(3):
            if self.arrayItem[i]==None:
                break
            elif self.arrayItem[i].data == key:
                return self.arrayItem[i]
        return -1 #ga ik nodig hebben bij retrieve

    #de gezochte item verwijderen uit een knoop
    #heb ik niet meer nodig
    def removeItem(self, delItem):
        delKey = delItem.data
        for i in range(3):
            thisKey = self.arrayItem[i].data
            if delKey == thisKey:
                self.arrayItem[i] = None
                self.numOfItems -= 1
                return True
        return False

    # toevoegen van item in op de juiste plaats binnen een knoop
    # vergelijkt de zoeksleutel van newItem met de items van de knopen en als het kleiner is dan verschuif(kopieer) item naar rechts als het groter is
    # dan voeg het toe op de volgende positie
    #return index, dit ga ik nodig hebben voor split functie
    def insertItem(self, newItem):
        self.numOfItems += 1 #add new item
        newKey = newItem.data #zoekssleutel van de nieuwe item
        for i in reversed(range(3)): #begin van rechts
            #als item leeg is, ga eentje naar links
            if self.arrayItem[i] == None:
                pass
            #als item niet leeg is
            else:
                thisKey = self.arrayItem[i].data   #zoeksleutel van item op pos i
                if newKey < thisKey:
                    self.arrayItem[i+1] = self.arrayItem[i]  #schuif item op pos i eentje naar rechts
                else:
                    self.arrayItem[i+1] = newItem   #insert new item
                    return i+1      #return pos index

        #nadat alle items zijn verschoven
        self.arrayItem[0] = newItem  # insert new item
        return 0    #return pos index

    #knoop is een blad
    def isLeaf(self):
        return not self.arrayChild[0] #als eerste item van array van knopen leeg is

    #get number of items
    def getnumOfItems(self):
        return self.numOfItems

    #get item at positie i van een knoop
    def getItem(self, i):
        return self.arrayItem[i]

    #get de i-de child van een knoop
    def getChild(self, i):
        return self.arrayChild[i]

    #bepalen of een knoop vol is
    def isVol(self):
        return self.numOfItems == 3

    #geef de ouder van een knoop
    def getParent(self):
        return self.parent

    #verwijder een kind(knoop) op een bepaalde positie en return it(ga ik nodig hebben bij insert)
    def removeChild(self, pos):
        tempNode = self.arrayChild[pos]
        self.arrayChild[pos] = None
        return tempNode

    #voeg een kind toe op een bepaalde positie
    #vergeet niet ouder van child is het object zelf
    def insertChild(self, pos, child):
        self.arrayChild[pos] = child
        if child != None:
            child.parent = self

    #temporarily verwijder item met grootste zoeksleutel en return it
    #ga ik nodig hebben voor split functie
    def deleteItem(self):
        temp = self.arrayItem[self.numOfItems - 1] #store grootste item in temp
        self.arrayItem[self.numOfItems - 1] = None
        self.numOfItems -= 1    #verminder aantal items met 1
        return temp

    #inorder traversal
    def inorderitem(self):
        inorder_lijst = []
        if self.isLeaf():
            for i in range(self.numOfItems):
                #of self.arrayItem[i].data werkt ook, overal waar ik getItem gebruik, als k vervang door arrayItem dan zou het ook werken
                inorder_lijst.append(self.getItem(i).item)
            return inorder_lijst
        if not self.isLeaf():
            for i in range(4):
                if self.getChild(i) != None:
                        inorder_lijst += self.getChild(i).inorderitem()
                #i<=2 is voor de aarayItem[i](ouder) toe te voegen
                if i<=2 and self.arrayItem[i]!=None:
                    inorder_lijst.append(self.arrayItem[i].item)
        return inorder_lijst

class Twee34Boom:
    def __init__(self):
        self.root = Node()

    def insert(self, value,item):
        """
        Voeg een data item toe op de juiste plaats
        :param value: Value die we gaan toevoegen
        """
        currentNode = self.root     #begin van wortel
        tempItem = ItemValue(value,item)
        while True:
            #knoop is vol
            if currentNode.isVol():
                self.split(currentNode)     #split de knoop
                #parent is een knoop
                currentNode = currentNode.getParent()
                currentNode = self.get_next_child(currentNode, value)
            #knoop is een blad
            elif currentNode.isLeaf():
                break
            #knoop is geen blad en niet vol
            else:
                currentNode = self.get_next_child(currentNode, value)

        currentNode.insertItem(tempItem)  #insert item

    def get_next_child(self, node, value):
        """
        Geef de kind van een node die uiteindelijk zal leiden tot de gezochte kind
        :param node: node waarvan we de juiste kind gaan vinden
        :param value: value om te vergelijken met data van de items
        :return: node
        """
        numOfItems = node.getnumOfItems()
        for i in range(numOfItems):
            if value < node.getItem(i).data:
                return node.getChild(i)     #return linker kind
        else:
            return node.getChild(i + 1) #return rechter kind

    def inorder_successor(self, node, pos):
        """
        Vind de inordersuccesor en return it
        :param node: knoop waar de item zit waarvan we de successor node gaan vinden
        :param pos: pos van de item waarvan we de successor node gaan vinden
        :return: successor node
        """
        rightChild = node.getChild(pos+1)
        while True:
            if rightChild.isLeaf():
                break
            else:
                rightChild = rightChild.getChild(0)
        return rightChild

    def remove(self, value):
        """
        Verwijder de item van de input value
        :param value: Value van item die gaan verwijderen
        :return: True als remove gelukt is, anders False
        """
        currentNode = self.root
        if currentNode == None: #root is empty
            return False
        while True:
            if currentNode == None:  # root is empty
                return False
            temp=currentNode.retrieveItem(value)
            if temp!=-1:
                if currentNode.retrieveItem(value).data == value:
                    break
            else:
                currentNode = self.get_next_child(currentNode, value)
        # currentnode is nu de juiste nood waar de delete element zit
        for i in range(currentNode.getnumOfItems()):
            if (currentNode.arrayItem[i].data == value):
                delPOs = i

        # nu weet je de node en de index van de element to delete
        if currentNode.isLeaf():    #knoop is blad, ga verder
            #currentNode.removeItem(currentNode.arrayItem[delPOs])
            for i in range(currentNode.getnumOfItems()):
                if i == 2:
                    break
                if currentNode.arrayItem[i + 1] != None:
                    currentNode.arrayItem[i] = currentNode.arrayItem[i + 1]
            currentNode.arrayItem[i] = None
            currentNode.numOfItems -= 1
            return True

        #eerst swappen met inorder successor
        elif not currentNode.isLeaf():
            #IO de inorder successor node, IO is altijd een leaf
            #returnt een node, de IO node
            IO = self.inorder_successor(currentNode, delPOs)
            #data van to delete item overschrijven door de inorder successor
            currentNode.arrayItem[delPOs] = IO.arrayItem[0]
            #schuif de andere kinderen eentje naar links als ze bestaan
            for i in range(IO.getnumOfItems()):
                if i == 2:
                    break
                if IO.arrayItem[i+1] != None:
                    IO.arrayItem[i] = IO.arrayItem[i+1]
            IO.arrayItem[i] = None
            IO.numOfItems -= 1
            return True

    def split(self, sNode):
        """
        Splits een knoop dat vol zit
        :param sNode:Knoop die we gaaan splitsen
        """
        # telkens grootste item verwijderen uit de volle knoop en store in item3 en item2 respectively
        grootste_item = sNode.deleteItem()
        middelste_item = sNode.deleteItem()
        #verwijder de twee kinderen op pos 2 en 3 van de volle knoop en store in kind2 en kind3
        kind2 = sNode.removeChild(2)
        kind3 = sNode.removeChild(3)

        #maak een nieuwe node
        newNode = Node()

        if sNode == self.root:  #als de voormalige volle knoop een root is, maak nieuwe root
            self.root = Node()
            parent = self.root  #root wordt de ouder
            self.root.insertChild(0,sNode) #voeg de overige item van de volle knoop als een kind toe aan de root
        else:
            parent = sNode.getParent()  #geef de ouder

        # voeg middelste item toe op de parent op zijn juiste plaats
        # itemPos bevat de index van de toegevoegde item
        itemPos = parent.insertItem(middelste_item)
        i = parent.getnumOfItems() - 1
        while i > itemPos:
            temp = parent.removeChild(i)
            parent.insertChild(i+1, temp)   #schuif de kind met eentje naar rechts
            i -= 1

        #voeg nieuwe kind toe aan de ouder
        parent.insertChild(itemPos+1, newNode)
        #ken een waarde toe aan de knoop
        newNode.insertItem(grootste_item)
        #voeg kinderen toe aan de knoop
        newNode.insertChild(0,kind2)
        newNode.insertChild(1,kind3)

    def retrieve(self, key):
        """
        Geef het item van een 2-3-4 boom, momenteel print ook found of not found om gemakkelijk te testen of het werkt
        :param key: Waarde dat we zoeken
        :return: Return type boolean, true als het gevonden is, anders false
        """
        currentNode = self.root     #begin van wortel
        while True:
            child = currentNode.retrieveItem(key)
            if child != -1:     #gevonden
                #print(key, "Found")
                return child
            elif currentNode.isLeaf():  #niet gevonden
                #print(key,"not found")
                return False
            else:
                currentNode = self.get_next_child(currentNode, key)   #zoek een niveau dieper

    def traverse(self):
        """
        Inorder traversal
        :return: lijst van data items
        """
        if self.isEmpty()==False:
            return self.root.inorderitem()
        return []

    def isEmpty(self):
        """
        Check of boom leeg is
        :return:True als boom leeg is, anders false
        """
        if self.root.getItem(0) == None:
            #print("true")
            return True
        else:
            #print("false")
            return False

    def destroy_tree(self):
        """
        Verwijder de boom
        """
        self.__init__()

    def getSize(self):
        return len(self.root.inorderitem())

if __name__ == "__main__":
    # maak een 234boom
    a = Twee34Boom()
    #return true
    a.isEmpty()
    #voeg deze waarden toe
    a.insert(15,15)
    a.insert(25,25)
    a.insert(45,45)
    a.insert(10,10)
    a.insert(40,40)
    a.insert(8,8)
    a.insert(20,20)
    a.insert(1,1)
    a.insert(5,5)
    a.insert(50,50)
    a.insert(30,30)
    a.insert(21,21)
    a.insert(31,31)
    # return false
    a.isEmpty()
    # geeft alle data items van de boom weer
    print(a.traverse())
    #return true en print ook found
    a.retrieve(50)
    a.retrieve(45)
    #return false en print not found
    a.retrieve(780)
    a.retrieve(945)
    #verwijdert 40
    a.remove(25)
    #geeft alle data items in de boom weer
    print(a.traverse())
    # return false en print not found
    a.retrieve(25)

    a.remove(10)
    print(a.traverse())
    a.retrieve(10)
    a.remove(45)
    print(a.traverse())
    a.retrieve(45)
    a.insert(100,100)
    a.insert(70, 70)
    a.insert(80, 80)
    a.insert(78, 78)
    print(a.traverse())
    a.isEmpty()
    #verwijder de boom
    a.destroy_tree()
    #return true
    a.isEmpty()


