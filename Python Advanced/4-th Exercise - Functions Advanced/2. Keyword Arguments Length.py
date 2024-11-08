def kwargs_length(**string):
    return len(string)


dictionary = {'name': 'Peter', 'age': 25}

print(*dictionary)
print(kwargs_length(**dictionary))


