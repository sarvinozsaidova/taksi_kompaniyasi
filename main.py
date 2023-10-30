from taxicompany import TaxiCompany
from taxi import Taxi
from place import Place
from passenger import Passenger


if __name__ == '__main__':
    company = TaxiCompany()
    
    taxi1 = Taxi(1)
    # taxi3 = Taxi(1)
    company.addTaxi(taxi1)
    # company.addTaxi(taxi2)
    # company.addTaxi(taxi3)

    
    place1 = Place('Yunusabot', 'Amir Temur')
    passenger1 = Passenger(place1)
    # passenger2 = Passenger(place2)
    
    taxi = company.callTaxi(passenger1)
    if taxi is not None:
        taxi.endTrip()
    else:
        company.lost_trips += 1
    
    
    print(f"Bekor qilingan chaqiruvlar soni {company.getLostTrips()}")
    

