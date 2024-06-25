for i in range(1, 15):
    if i % 2 == 0:
        print(i)




def func1():
    print("edited on github")


def outer(func):
    def inner():
        print("*******")
        func()
        print("#######")

    return inner


@outer
def func_test():
    print("inside func")
