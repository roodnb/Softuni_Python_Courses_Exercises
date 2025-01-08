class A:

    def hi(selfs):
        return "from class a Hi"

class B:
    def hi(selfs):
        return "from class b hi"

class C(B, A):
    pass

c = C()
print(c.hi())

print(C.__mro__)
