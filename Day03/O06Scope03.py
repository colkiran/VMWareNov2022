
def outerFun(gname):                   # local variable

    def innerFun():
        nonlocal gname                 # only local variables can be                                    converted into nonlocal variables
        gname += " Dravid"
        guest = f"Mr.{gname}"
        print("Hello World")
        print(gname)
        print(f"Greetings {guest}")

    innerFun()
    print(f"After :{gname}")

outerFun("Rahul")
