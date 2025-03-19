from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = next((cust for cust in self.customers if cust.id == customer_id), None)
        current_dvd = next((doovde for doovde in self.dvds if doovde.id == dvd_id), None)

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd not in current_customer.rented_dvds and current_dvd.is_rented:
            return "DVD is already rented"

        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = next((cust for cust in self.customers if cust.id == customer_id), None)
        current_dvd = next((doovde for doovde in self.dvds if doovde.id == dvd_id), None)

        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"

        return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for cust in self.customers:
            result.append(cust.__repr__())

        for dvd in self.dvds:
            result.append(dvd.__repr__())

        return "\n".join(result)
