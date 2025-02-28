from project.dvd import DVD


class Customer:

    def __init__(self,name: str, age: int, id: int) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds: list[DVD] = []

    def __repr__(self):
        titles = ', '.join(dvd.name for dvd in self.rented_dvds)
        return (f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} "
                f"rented DVD's ({titles})")