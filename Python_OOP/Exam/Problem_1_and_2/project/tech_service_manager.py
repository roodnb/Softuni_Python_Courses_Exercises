from project.devices.base_device import BaseDevice
from project.devices.laptop import Laptop
from project.devices.smartphone import Smartphone
from project.devices.smartwatch import Smartwatch
from project.repair_shop import RepairShop


class TechServiceManager:
    valid_device = {"Laptop": Laptop, "Smartphone": Smartphone, "Smartwatch": Smartwatch}

    def __init__(self):
        self.devices: list[BaseDevice] = []
        self.repair_shops: list[RepairShop] = []

    def add_device(self, device_type: str, serial_number: str, durability: int, is_functional: bool):
        if device_type not in self.valid_device:
            raise ValueError("Invalid device type!")

        dev = self.valid_device[device_type](serial_number, durability, is_functional)
        dev.check_functionality()
        self.devices.append(dev)
        return f"{device_type} is successfully added."

    def add_repair_shop(self, name: str, device_types: tuple):
        # check this login
        if len(device_types) < 0 or not any(dev in self.valid_device for dev in device_types):
            raise ValueError("No valid device type!")

        # current_valid_devices = tuple(dev_type for dev_type in device_types if dev_type in self.valid_device)

        shop = RepairShop(name, device_types)
        self.repair_shops.append(shop)
        return f"{name} is successfully added as a repair shop."

    def send_for_repair(self, repair_shop_name: str, device_type: str):
        searched_shop = [shop for shop in self.repair_shops if shop.name == repair_shop_name][0]

        if device_type not in searched_shop.device_types:
            return "The shop cannot repair this device type."

        all_devices_of_same_type = [dev for dev in self.devices if dev.device_type == device_type]

        try:
            searched_dev = [dev for dev in all_devices_of_same_type if dev.is_functional == False][0]
            self.devices.remove(searched_dev)
            searched_shop.pending_devices.append(searched_dev)
            return f"{searched_dev.serial_number} was sent for repair to {repair_shop_name}."
        except IndexError:
            return f"There is no {device_type} that needs repair."

    @staticmethod
    def process_repairs(repair_shop: RepairShop):
        return repair_shop.repair()

    def receive_repaired_devices(self, repair_shop: RepairShop):
        count = 0
        while len(repair_shop.repaired_devices) > 0:
            removed_device = repair_shop.repaired_devices.pop()
            self.devices.append(removed_device)
            count += 1
        return f"Received {count} repaired devices"

    def tech_service_status(self):
        result = "***Tech Service***\n"

        managers_functional_devices_count = len([dev for dev in self.devices if dev.is_functional == True])
        result += f"Total number of functional devices: {managers_functional_devices_count}\n"

        managers_malfunctioning_devices_count = len([dev for dev in self.devices if dev.is_functional == False])
        result += f"Total number of malfunctioning devices: {managers_malfunctioning_devices_count}\n"

        result += f"Repair shops count: {len(self.repair_shops)}"

        sorted_shops = sorted(self.repair_shops, key=lambda x: x.name)

        for s in sorted_shops:
            result += f"\n@{s.status()}"

        return result
