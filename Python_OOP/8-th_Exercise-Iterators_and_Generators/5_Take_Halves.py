def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            result = i / 2
            yield result

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result

    return (take, halves, integers)



take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

print(f"\n{'-----------------------------NEW TEST CODE-----------------------------'}")

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
