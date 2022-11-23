
def outerFun(gname):        # HOF - Higher Order Function

    def innerFun():
        # print("hello world")
        print(f"Greetings Mr.{gname}")

    return innerFun


infun = outerFun("Sachin")
print("after few lines of code......")

infun()
print("-" * 40)

outerFun("Rahul")()             # calls the inner function

print("-" * 40)

print(outerFun.__name__)
print(outerFun("Sourav").__name__)