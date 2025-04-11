from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)
        self.type = "Royal"

    def zone_info(self):
        pirateships = [p for p in self.ships if p.__class__.__name__ == "PirateBattleship"]

        result = f"@Royal Zone Statistics@\n"
        result += (f"Code: {self.code}; Volume: {self.volume}\n"
                   f"Battleships currently in the Royal Zone: {len(self.ships)}, "
                   f"{len(pirateships)} out of them are Pirate Battleships.")

        ordered_battleships = self.get_ships()
        result += f"\n#{', '.join([s.name for s in ordered_battleships])}#" if ordered_battleships else ""
        return result
