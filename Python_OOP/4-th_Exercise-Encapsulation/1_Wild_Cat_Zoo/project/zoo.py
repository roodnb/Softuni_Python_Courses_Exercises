from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker_to_be_fired = [worker for worker in self.workers if worker.name == worker_name][0]
            self.workers.remove(worker_to_be_fired)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(worker.salary for worker in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_to_care = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= total_money_to_care:
            self.__budget -= total_money_to_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def __print_status(self,obj_list: list[Animal | Worker], *class_names: str):
        element = {name: [] for name in class_names}
        for obj in obj_list:
            element[obj.__class__.__name__].append(repr(obj))
        result = f"You have {len(obj_list)} {str(obj_list[0].__class__.__bases__[0].__name__).lower()}s"

        for k, v in element.items():
            result += f"\n----- {len(v)} {k}s:"
            for value in v:
                result += f"\n{value}"

        return result

    def animals_status(self):
        # lions = []
        # tigers = []
        # cheetahs = []
        # for animal in self.animals:
        #     if animal.__class__.__name__ == "Lion":
        #         lions.append(repr(animal))
        #     elif animal.__class__.__name__ == "Tiger":
        #         tigers.append(repr(animal))
        #     elif animal.__class__.__name__ == "Cheetah":
        #         cheetahs.append(repr(animal))
        #
        # result = [f"You have {len(self.animals)} animals"]
        # result.append(f"----- {len(lions)} Lions:")
        # result.extend(lions)
        # result.append(f"----- {len(tigers)} Tigers:")
        # result.extend(tigers)
        # result.append(f"----- {len(cheetahs)} Cheetah:")
        # result.extend(cheetahs)
        # return '\n'.join(result)
        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")
    def workers_status(self):
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")


