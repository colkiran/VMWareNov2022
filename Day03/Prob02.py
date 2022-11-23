
import time

def timeCalc(fnc):

    def helper(max):
        st = time.perf_counter()
        fnc(max)
        et = time.perf_counter()
        print(f"The total time taken is {et - st}")

    return helper

@timeCalc
def fun(max):
    lst = []
    for i in range(1, max):
        for j in range(1, i+1):
            lst.append(j ** 2)

fun(5500)