def f():
    yield 1
    yield 2
    yield 3

for x in f():
    print(x)

for x in f():
    print(x)