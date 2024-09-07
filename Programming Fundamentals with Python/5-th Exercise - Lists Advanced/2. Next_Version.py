version = (''.join(input().split('.')))
new_version = int(version) + 1
new_version_string = list(str(new_version))
print('.'.join(new_version_string))