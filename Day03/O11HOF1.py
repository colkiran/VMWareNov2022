
def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def outerFun(fnc):
    loginfo = "Logging into the service....."

    def innerFun(*args):
        print(loginfo)
        print(fnc(*args))               # CALL BACK
        print("-" * 40)

    return innerFun

sumlogger = outerFun(sum)
sumlogger(65, 85)
print("-" * 40)

difflogger = outerFun(diff)
difflogger(250, 185)
