
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

kanGrt = outerFun("Namaskara")
kantgr = kanGrt("lion")
kantgr("Prabhakar")


"""
engGrt = outerFun("Welcome")
tmlGrt = outerFun("Vanakam")


snglnEng = engGrt("----->")
snglnEng("Sachin")

snglnTml = tmlGrt("----->")
snglnTml("Dhoni")


"""