from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def team_data(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        expenses, sponsors = self.team_data
        for sponsor in sponsors.values():
            for position, price in sponsor.items():
                if race_pos <= position:
                    revenue += price
                    break
        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
