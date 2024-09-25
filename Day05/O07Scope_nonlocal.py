
def outerFun():
    gname = "Jordan"            # local variable
    def innerFun():
        nonlocal gname          # only local variable can be converted                          to non_local variables
        gname = "Micheal " + gname

        print("Hello World")
        print(f"Greetings {gname}")


    innerFun()
    print(f"outerfun :{gname}")


outerFun()
