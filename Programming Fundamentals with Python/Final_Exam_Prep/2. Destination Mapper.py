import re
places = input()
pattern = r'([=|\/])([A-Z][A-Za-z]{2,})\1'

matches = re.finditer(pattern, places)
total_sum = 0
valid_places = []
for match in matches:
    total_sum += len(match.group(2))
    valid_places.append(match.group(2))
print(f"Destinations: {', '.join(valid_places)}\n"
      f"Travel Points: {total_sum}")