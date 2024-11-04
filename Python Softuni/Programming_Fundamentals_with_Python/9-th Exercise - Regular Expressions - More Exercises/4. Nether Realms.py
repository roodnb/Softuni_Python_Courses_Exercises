import re

pattern_health = r"[^\d\+\-\*\/\.]"
pattern_damage = r"([-+]?\d+(\.\d+)?)"
pattern_operator = r"[*\/]"

demons = input().split(",")
demons = [demon.strip() for demon in demons]

for demon in sorted(demons):
    health = re.findall(pattern_health, demon)
    health = sum(ord(character) for character in health)
    damage = re.findall(pattern_damage, demon)

    if damage:
        damage = sum(float(number[0]) for number in damage)

        operators = re.findall(pattern_operator, demon)

        if operators:
            for operator in operators:
                if operator == "*":
                    damage *= 2
                elif operator == "/":
                    damage /= 2

    else:
        damage = 0
    print(f"{demon} - {health} health, {damage:.2f} damage")