from collections import deque
string_expression = input().split()
queue = deque()


def calculate(n_1, n_2, op):
    if op == "+":
        return n_1 + n_2
    elif op == "-":
        return n_1 - n_2
    elif op == "*":
        return n_1 * n_2
    elif op == "/":
        return n_1 // n_2


for index in string_expression:
    if index not in '+-*/':
        queue.append(int(index))
    else:
        while len(queue) > 1:
            num_1 = queue.popleft()
            num_2 = queue.popleft()
            queue.appendleft(calculate(num_1, num_2, index))

print(queue.popleft())