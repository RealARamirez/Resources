# From the first file
def float_tester(arg):
    NumArg = str(arg).strip(" ").strip("\t")
    for elem in NumArg.split("."):
        if elem.isdigit():
            Answer = True
        else:
            Answer = False
            break
    return Answer
# Calculate the minimum of a list avoiding elements that cannot be converted to a float
def maximum(arg):
    auxiliar_list = []
    a = 0
    while a < len(arg):
        if str(arg[a]).isdigit() or float_tester(arg[a]):
            auxiliar_list.append(float(arg[a]))
            c += 1
        else:
            c += 1
    return max(auxiliar_list)
# Calculate the maximum of a list avoiding the elements that cannot be converted to a float
def minimum(arg):
    auxiliar_list = []
    a = 0
    while a < len(arg):
        if str(arg[a]).isdigit() or float_tester(arg[a]):
            auxiliar_list.append(float(arg[a]))
            c += 1
        else:
            c += 1
    return min(auxiliar_list)

