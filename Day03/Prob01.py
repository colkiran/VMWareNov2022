

def check_max(fnc):

    def helper(a, b):

        if b > a:
            a, b = b, a
        print(fnc(a, b))

    return helper


@check_max
def diff(x, y):
    return x - y

diff(20, 10)
diff(10, 15)
diff(20, 35)
diff(8, 20)

print("*-" * 40)


def makepositive(fnc):
    def swap(x, y):
        if x > y:
            return fnc(x, y)
        else:
            return fnc(y, x)

    return swap


@makepositive
def diff(x, y):
    return x - y


print(diff(20, 55))
