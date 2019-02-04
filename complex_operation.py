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
# Calculate the average of a given list avoiding the elements that cannot be converted into a float
def average(arg):
    a = 0
    b = 0
    while a < len(arg):
        if str(arg[a]).isdigit() or float_tester(arg[a]):
            b = b + float(arg[a])
            a += 1
        else:
            a += 1
    return b/len(arg)
# Calculate the median of a given list avoiding the elements that cannot be converted into a float
def median(arg):
    auxiliar_list = []
    a = 0
    while a < len(arg):
        if str(arg[a]).isdigit() or float_tester(arg[a]):
            auxiliar_list.append(float(arg[a]))
            a += 1
        else:
            a += 1
    auxiliar_list = sorted(auxiliar_list)
    b = float(auxiliar_list[int(len(auxiliar_list)/2)])
    c = float(auxiliar_list[int((len(auxiliar_list)/2)-1)])
    if len(auxiliar_list) % 2 == 0:
        Sol = average([b, c])
    else:
        Sol = b
    return Sol


