import datetime

my_date = datetime.date(2016, 7, 11)

class Clothing:
    """
    The Clothing class defines a piece of clothing in terms of its
    name and its cleanliness.
    """
    amount_clothes=0 #statische Variable

    def __init__(self, name):
        self.name=name

    def getName(self,name):
        return self.name

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

class SportClothes(Clothing):

    amount_clothes = 0

    def __init__(self,name, price):
        super().__init__(name)
        self.price=price


def main():
    #test the Clothing Class
    myJeans = Clothing("blue jeans")
    myShorts = Clothing("shorts")
    running_shoes = SportClothes("Running Shoes",60)

if __name__ == "__main__":
    main()