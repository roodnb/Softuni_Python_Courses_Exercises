from project.Cls_id_mixin import Clsidmixin


class Customer(Clsidmixin):
    def __init__(self, name: str, address: str, email: str) ->None:
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        self.increment_id()

    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
