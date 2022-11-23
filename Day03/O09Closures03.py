
# HOF
def outerFun(greet):
    def innerFun(gname):
        print(greet, gname)
    return innerFun

outerFun("Welcome")("Sachin")
print("-" * 40)

# simple curry
engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")
tmlGrt = outerFun("Vanakam")


engGrt("Virat")
engGrt("Rohit")

hndGrt("Axar Patel")
tmlGrt("Natraj")