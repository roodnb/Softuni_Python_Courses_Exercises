from project.devices.base_device import BaseDevice


class Laptop(BaseDevice):
    device_type = "Laptop"

    def __init__(self, serial_number: str, durability: int, is_functional: bool):
        super().__init__(serial_number, durability, is_functional, self.device_type)

    def repair(self) -> None:
        if not self.is_functional and self.durability + 50 <= 100:
            self.durability = self.durability + 50
            self.is_functional = True
