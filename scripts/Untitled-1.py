
def abc_generator():
    yield("a")
    yield("b")
    yield("c")

MyObject= abc_generator()

print(MyObject.__next__())

print(MyObject.__next__())


