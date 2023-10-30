class Taxi:
    def __init__(self, id):
        self.id = id
        self.mavjud = True
    
    def __str__(self):
        return f"Taxi {self.id} chi"
    
    def startTrip(self, destination):
        self.mavjud = False
        print(f"{self} ga sayohat boshlandi {destination}")
    
    def endTrip(self):
        self.mavjud = True
        print(f"{self} sayohat tugagan")