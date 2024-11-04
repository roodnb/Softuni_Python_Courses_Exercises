title = input()
content = input()
commands = []
while True:
    command = input()
    if command == 'end of comments':
        break
    commands.append(command)

print(f'<h1>\n'
        f'    {title}\n'
        f'</h1>')
print(f'<article>\n'
        f'    {content}\n'
        f'</article>')

for current_command in commands:
    print(f'<div>\n'
          f'    {current_command}\n'
          f'</div>')
