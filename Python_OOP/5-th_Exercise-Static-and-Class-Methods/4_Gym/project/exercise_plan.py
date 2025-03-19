from project.Cls_id_mixin import Clsidmixin


class ExercisePlan(Clsidmixin):
    def __init__(self, trainer_id: int, equipment_id: int, duration: int) -> None:
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration  # the duration is in minutes
        self.id = self.get_next_id()
        self.increment_id()

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int) -> "ExercisePlan":
        duration_in_mins = hours * 60
        return cls(trainer_id, equipment_id, duration_in_mins)

    def __repr__(self) -> str:
        return f"Plan <{self.id}> with duration {self.duration} minutes"
