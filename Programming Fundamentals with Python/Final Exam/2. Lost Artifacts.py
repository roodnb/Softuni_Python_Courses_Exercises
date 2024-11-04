import re

artifact_info = input()
decoding_pattern = r'([*|^]([a-zA-Z\s]{6,})[*|^])(.*?)[\+]+([\-]*[\d]+[\.]*[\d]*)\,([\-]*[\d]+[\.]*[\d]*)[\+]+'
matches = re.findall(decoding_pattern, artifact_info)
if matches:
    for match in matches:
        artifact_name = match[1]
        latitude = match[3]
        longitude = match[4]
        print(f"Found {artifact_name} at coordinates {latitude},{longitude}.")
else:
    print("No valid artifacts found.")