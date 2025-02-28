from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self) -> None:
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []


    def check_availability(self,who, where: list):
        if who not in where:
            return True

    def get_the_thing(self, where, what):
        current_thing = next((t for t in where if t.id == what), None)
        return current_thing

    def add_customer(self, customer: Customer) -> None:
        if self.check_availability(customer, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if self.check_availability(trainer, self.trainers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if self.check_availability(equipment, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if self.check_availability(plan, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if self.check_availability(subscription, self.subscriptions):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        current_subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        current_customer = self.get_the_thing(self.customers, current_subscription.customer_id)
        current_trainer = self.get_the_thing(self.trainers, current_subscription.trainer_id)
        current_exercise_plan = self.get_the_thing(self.plans, current_subscription.trainer_id)
        current_equipment = self.get_the_thing(self.equipment, current_exercise_plan.equipment_id)

        result = [current_subscription.__repr__(), current_customer.__repr__(), current_trainer.__repr__(),
                  current_equipment.__repr__(), current_exercise_plan.__repr__()]
        return '\n'.join(result)
