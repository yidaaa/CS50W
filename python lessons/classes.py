# calling functions from another file
from basics import get_name

# creating new classes

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
        return self.capacity-len(self.passengers)

    def add_passenger(self, name):
        if self.open_seats()>0:
            self.passengers.append(name)
            return True
        else:
            return False

flight = Flight(3)
people = ["nartuo", "sasuke", "sakura", "kakashi"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No seats avaliable for {person}")