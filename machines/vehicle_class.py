class Vehicle:
    vehicle_count = 0

    def __init__(self, make, model):
        self.vehicle_make = make
        self.vehicle_model = model
        Vehicle.vehicle_count +=1

    def display_count(self):
        return Vehicle.vehicle_count


car1 = Vehicle('Toyota', 'Camary')
car2 = Vehicle('Nissan', 'Pathfinder')
print(car1.display_count())
