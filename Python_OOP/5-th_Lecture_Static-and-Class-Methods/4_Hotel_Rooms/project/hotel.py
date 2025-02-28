from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: list[Room] = []
        # self.guests = 0 - tova go mahame zashtoto slagame dolnoto property

    @property
    def guests(self):
        return sum([room.guests for room in self.rooms]) # shte vyrtim prez vsichki stai, shte sumirame kolko
                                                        # gosti imame v sqka staq i shte gi sumirame.
                                                        # ponene toq metod e @property. vseki pyt kogato nqkoi go
                                                        # vikne to shte vryshta total sumata.

    @classmethod
    def from_stars(cls, stars_count: int) -> "Hotel":
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number, people) -> None:
        room_to_find = [room for room in self.rooms if room.number == room_number][0]
        return room_to_find.take_room(people) # take_room metoda e tozi ot klasa room a ne ot klasa hotel, a go
                                             # vryshtame, zashtoto syshtiq metod v klasa room ima opciq za return str

    def free_room(self, room_number):
        room_to_find = [room for room in self.rooms if room.number == room_number][0]
        return room_to_find.free_room() # free_room metoda e tozi ot klasa room a ne ot klasa hotel

    def status(self) -> str:
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        result = (f"Hotel {self.name} has {self.guests} total guests\n"
                  f"Free rooms: {', '.join(free_rooms)}\n"
                  f"Taken rooms: {', '.join(taken_rooms)}")

        return result
