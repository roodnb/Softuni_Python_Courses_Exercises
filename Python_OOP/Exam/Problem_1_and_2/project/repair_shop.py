from project.devices.base_device import BaseDevice


class RepairShop:
    def __init__(self, name: str, device_types: tuple) -> None:
        self.name = name
        self.device_types = device_types
        self.pending_devices: list[BaseDevice] = []
        self.repaired_devices: list[BaseDevice] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Invalid repair shop name!")
        self.__name = value

    @property
    def device_types(self):
        return self.__device_types

    @device_types.setter
    def device_types(self, value):
        if len(value) < 1:
            raise ValueError("No device types provided!")
        self.__device_types = value

    def repair(self) -> str:
        count = 0
        while len(self.pending_devices) > 0:
            for device in self.pending_devices:
                device.repair()
                self.pending_devices.remove(device)
                self.repaired_devices.append(device)
                count += 1
        return f"Repaired {count} device/s."

    def status(self) -> str:
        return (f"{self.name} has {len(self.pending_devices)} devices pending for repair "
                f"and {len(self.repaired_devices)} devices repaired.")
