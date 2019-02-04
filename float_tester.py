def float_tester(arg):
    NumArg = str(arg).strip(" ").strip("\t")
    for elem in NumArg.split("."):
        if elem.isdigit():
            Answer = True
        else:
            Answer = False
            break
    return Answer

