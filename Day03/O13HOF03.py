
def funlogger(fnc):

    def helper():
        print("Logging into a service............")
        fnc()       # call back
        print("-"  * 40)
    return helper


def normalfun():
    print("Call me Normal Function.........")


normalFun = funlogger(normalfun)
normalFun()


@funlogger
def basicFun():
    print("call me Basic Function.............")


basicFun()