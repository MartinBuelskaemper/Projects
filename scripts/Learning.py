import datetime

my_date = datetime.date(2016, 7, 11)

class Clothing(object):
    """
    The Clothing class defines a piece of clothing in terms of its
    name and its cleanliness.
    """
    amount_clothes=0 #statische Variable

    def __init__(self, name, clean=True):
        self.name=name
        self.clean=clean

    def getName(self,name):
        return self.name

    def isClean(self,clean):
        return self.clean

    @classmethod
    def raiseAmount(cls,amount):
        """
        funktioniert für alle Objekte der Klasse
        und setzt jeweils die amount_clothes = amount
        self hingegen ist das Stichwort für ein Objekt.
        Im Endeffekt gibt es also Klassenvariablen, Instanzvariablen,
        Klassenmethoden und Instanzmethoden.
        """
        cls.amount_clothes = amount
    
    @staticmethod
    def is_workday(day):
        """
        Hat eine Funktion in der Klasse, aber ist nicht direkt mit
        ihr verknüpft.
        """
        if day.weekday() in range(5,7):
            return False
        return True


def main():
    #test the Clothing Class
    myJeans = Clothing("blue jeans",False)
    myShorts = Clothing("shorts")
    print(Clothing.is_workday(my_date))

if __name__ == "__main__":
    main()