def max2(*x):
    list_1 = []
    for i in x:
        list_1.append(i)
    a = list_1[0]
    for i in list_1:
        if i > a:
            a = i
    return a

