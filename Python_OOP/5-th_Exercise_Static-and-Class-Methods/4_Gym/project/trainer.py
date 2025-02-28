from project.Cls_id_mixin import Clsidmixin


class Trainer(Clsidmixin):

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = self.get_next_id()
        self.increment_id()

    def __repr__(self) -> str:
        return f"Trainer <{self.id}> {self.name}"
