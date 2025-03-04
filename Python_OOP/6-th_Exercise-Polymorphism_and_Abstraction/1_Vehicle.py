from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption  # liters per km

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 0.9)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 1.6)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)

