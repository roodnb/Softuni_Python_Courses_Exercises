from project.player import Player
from project.guild import Guild


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())




player = Player("Pesho", 90, 90)
print(player.add_skill("A", 3))
print(player.add_skill("A", 3))
print(player.player_info())

guild = Guild("GGXrd")
print(guild.assign_player(player))
print(guild.assign_player(player))