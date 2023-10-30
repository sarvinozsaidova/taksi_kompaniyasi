from invalidtaxiname import InvalidTaxiName
from taxi import Taxi
from passenger import Passenger
from trip import Trip

class TaxiCompany:
    def __init__(self):
        self.taxis = []
        self.lost_trips = 0
    
    def addTaxi(self, taxi :Taxi):
        for t in self.taxis:
            if t.id == taxi.id:
                raise InvalidTaxiName("bunday id avvaldan mavjud")
        self.taxis.append(taxi)
    
    def getAvailable(self):
        return [taxi for taxi  in self.taxis if taxi.mavjud]
    
    def callTaxi(self, passenger : Passenger):
        mavjud_taxis = self.getAvailable()
        if len(mavjud_taxis) == 0:
            print("bo`sh taksi yoq. chaqiruv bekor qilindi")
            return None
        else:
            taxi = mavjud_taxis[0]
            taxi.startTrip(passenger.getPlace())
            return taxi
    
    def getLostTrips(self):
        return self.lost_trips
    
    def getTrips(self, taxi_id : Taxi):
        taxi = None
        for t in self.taxis: 
            if t.id == taxi_id:
                taxi = t
                break
        if taxi is None:
            raise InvalidTaxiName("bunday id taksi mavjud emas")
        return [trip for trip in self.trips if trip.taxi == taxi]
    