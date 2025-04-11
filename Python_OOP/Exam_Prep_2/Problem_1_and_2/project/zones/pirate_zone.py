from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self,code: str):
        super().__init__(code, self.INITIAL_VOLUME)
        self.type = "Pirate"

    def zone_info(self):

        royalships = [p for p in self.ships if p.__class__.__name__ == "RoyalBattleship"]

        result = f"@Pirate Zone Statistics@\n"
        result += (f"Code: {self.code}; Volume: {self.volume}\n"
                   f"Battleships currently in the Pirate Zone: "
                   f"{len(self.ships)}, "
                   f"{len(royalships)} out of them are Royal Battleships.")

        ordered_battleships = self.get_ships()

        result += f"\n#{', '.join([s.name for s in ordered_battleships])}#" if ordered_battleships else ""
        return result
