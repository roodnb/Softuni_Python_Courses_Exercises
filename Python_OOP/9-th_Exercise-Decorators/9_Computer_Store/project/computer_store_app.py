from project.computer_types.computer import Computer
from project.computer_types.laptop import Laptop
from project.computer_types.desktop_computer import DesktopComputer


class ComputerStoreApp:
    VALID_COMP_TYPES: dict[str, type[Computer]] = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self) -> None:
        self.warehouse: list[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor:  str, ram: int):
        if type_computer not in self.VALID_COMP_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        current_computer = self.VALID_COMP_TYPES[type_computer](manufacturer, model)
        result = current_computer.configure_computer(processor, ram)
        self.warehouse.append(current_computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        # for comp in self.warehouse:
        #     if client_budget >= comp.price and wanted_processor == comp.processor and wanted_ram <= comp.ram:
        #         self.profits += client_budget - comp.price
        #         self.warehouse.remove(comp)
        computer = next((comp for comp in self.warehouse if client_budget >= comp.price
                         and wanted_processor == comp.processor and wanted_ram <= comp.ram), None)
        if computer:
            self.profits += client_budget - computer.price
            self.warehouse.remove(computer)
            return f"{computer.__repr__()} sold for {client_budget}$."
        else:
            raise Exception("Sorry, we don't have a computer for you.")
