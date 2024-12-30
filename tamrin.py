from os import name
import random

class Car:
    def init(self, car_id, fuel, max_speed, color):
        self.car_id = car_id
        self.fuel = fuel
        self.max_speed = max_speed
        self.color = color
        self.distance_covered = 0
        self.active = True
        self.finished = False

    def drive(self):
        if self.fuel > 0 and self.active:
            self.distance_covered += self.max_speed
            self.fuel -= 1

    def refuel(self):
        if self.active:
            self.fuel += 3

    def refuel_at_station(self, next_station_distance):
        if self.active:
            probability = self.calculate_probability(next_station_distance)
            if probability < 0.5:
                self.refuel()

    def calculate_probability(self, next_station_distance):
        distance_possible = self.fuel * self.max_speed
        probability = min(1, distance_possible / next_station_distance)
        return probability

    def check_fuel(self):
        if self.fuel <= 0 and self.active:
            self.active = False
            print(f"Car {self.car_id} ({self.color}) is out of fuel and out of the race.")

    def str(self):
        return f"Car {self.car_id} ({self.color}): Distance = {self.distance_covered}, Fuel = {self.fuel}"

def race(cars, fuel_stations, track_length):
    finish_order = []
    while any(car.active for car in cars):
        for station in fuel_stations:
            for car in cars:
                if car.active:
                    car.drive()
                    if car.distance_covered >= station:
                        next_station_distance = fuel_stations[fuel_stations.index(station) + 1] - station if fuel_stations.index(station) + 1 < len(fuel_stations) else track_length - station
                        car.refuel_at_station(next_station_distance)
                car.check_fuel()

            for car in cars:
                if car.distance_covered >= track_length and car.active:
                    car.finished = True
                    car.active = False
                    finish_order.append(car)

    finish_order.sort(key=lambda x: x.distance_covered, reverse=True)

    print("Race finished. Results:")
    for i, car in enumerate(finish_order):
        print(f"{i+1}. Car {car.car_id} ({car.color}): Distance = {car.distance_covered}, Fuel = {car.fuel}")

if name == "main":
    num_cars = 10
    track_length = 1000
    fuel_stations = [200, 500, 800]

    colors = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Purple", "Orange", "Gray", "Pink"]

    cars = [
        Car(
            car_id,
            random.choice([30, 35, 40, 45, 50]),
            random.randint(250, 300),
            colors[car_id - 1]
        ) for car_id in range(1, num_cars + 1)
    ]
    
    race(cars, fuel_stations, track_length)
