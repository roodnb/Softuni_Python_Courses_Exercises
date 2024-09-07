player_position_skill = {}
command = input()
while command != 'Season end':

    if " -> " in command:
        current_command = command.split(' -> ')
        player = current_command[0]
        position = current_command[1]
        skill = int(current_command[2])

        if player not in player_position_skill:
            player_position_skill[player] = {position: skill}
        elif position not in player_position_skill[player].keys():
            player_position_skill[player][position] = skill
        elif skill > player_position_skill[player][position]:
            player_position_skill[player][position] = skill


    elif ' vs ' in command:
        player_one, player_two = command.split(' vs ')
        lose_plaer = None
        lose_skill = None
        if player_one in player_position_skill and player_two in player_position_skill:
            for p1 in player_position_skill[player_one]:
                for p2 in player_position_skill[player_two]:
                    if p1 == p2:
                        if player_position_skill[player_one][p1] == player_position_skill[player_two][p1]:
                            break
                        elif player_position_skill[player_one][p1] > player_position_skill[player_two][p1]:
                            lose_plaer = player_two
                            lose_skill = p1
                            break
                        elif player_position_skill[player_one][p1] < player_position_skill[player_two][p1]:
                            lose_plaer = player_one
                            lose_skill = p1
                            break
                if lose_plaer is not None:
                    del player_position_skill[lose_plaer][lose_skill]
                    lose_plaer = None
                    lose_skill = None
                else:
                    break

    command = input()

total_result_dict = {}
for k, v in player_position_skill.items():
    result_sum = 0
    for k1, v1 in player_position_skill[k].items():
        result_sum += v1
    total_result_dict[k] = result_sum
sorted_total_results = dict(sorted(total_result_dict.items(), key=lambda x: (-x[1], x[0])))

for key, value in sorted_total_results.items():
    if len(player_position_skill[key]) == 0:
        continue
    else:
        print(f'{key}: {value} skill')
    last_dict = {}
    for key1, value1 in player_position_skill[key].items():
        last_dict[key1] = value1
    sorted_last_dict = dict(sorted(last_dict.items(), key=lambda x: (-x[1], x[0])))
    for key2, value2 in sorted_last_dict.items():
        print(f'- {key2} <::> {value2}')




        # elif ' vs ' in command:
        # first_player, second_player = command.split(' vs ')
        #
        # if first_player in player_position_skill and second_player in player_position_skill:
        #     for first_key, first_value in player_position_skill[first_player].items():
        #         for second_key, second_value in player_position_skill[second_player].items():
        #             if first_key == second_key:
        #                 if first_value > second_value:
        #                     del player_position_skill[]
        #                     break
        #                 elif first_value < second_value:
        #                     del player_position_skill[first_key]
        #                     break
        #             break





# for player, totalSkill in sorted(player_position_skill.items(), key=lambda x: (-sum(i for i in x[1].values()), x[0])):
#     if len(player_position_skill[player]) == 0:
#         continue
#     else:
#         print(f'{player}: {sum(totalSkill.values())} skill')
#     for user, skill in sorted(player_position_skill[player].items(), key=lambda x: (-x[1], x[0])):
#         print(f'- {user} <::> {skill}')






