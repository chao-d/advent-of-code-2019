def foo():
    a = 1
    bar(a)
    print(a)


def bar(a):
    a += 1

foo()
