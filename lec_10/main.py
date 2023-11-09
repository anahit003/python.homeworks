from Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def move(self):
        print("The car is moving.")

    def stop(self):
        print("The car is stopping.")

class Plane(Vehicle):
    def __init__(self, make, model, year, wingspan):
        super().__init__(make, model, year)
        self.wingspan = wingspan

    def move(self):
        print("The plane is flying.")

    def stop(self):
        print("The plane is landing.")

class Boat(Vehicle):
    def __init__(self, make, model, year, length):
        super().__init__(make, model, year)
        self.length = length

    def move(self):
        print("The boat is sailing.")

    def stop(self):
        print("The boat is docking.")


class RaceCar(Car):
    def __init__(self, make, model, year, num_doors, engine_type):
        super().__init__(make, model, year, num_doors)
        self.engine_type = engine_type

    def accelerate(self):
        print("The race car is accelerating.")

    def brake(self):
        print("The race car is braking.")

       
car = Car("Toyota", "Camry", 2020, 4)
car.move()

plane = Plane("Airbus", "A310", 2021, 187)
plane.move()

boat = Boat("Viking", "Righteous Rage", 2021, 10)
boat.move()

race_car = RaceCar("Ferrari", "F1", 2023, 2, "V8")
race_car.accelerate()
race_car.brake()
