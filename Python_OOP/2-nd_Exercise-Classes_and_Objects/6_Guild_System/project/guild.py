from project.player import Player


class Guild:
    def __init__(self, name: str,):
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        try:
            current_player = [el for el in self.players if el.name == player_name][0]
            self.players.remove(current_player)
            current_player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        except IndexError:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}"
        for player in self.players:
            result += f"\n{player.player_info()}"

        return result