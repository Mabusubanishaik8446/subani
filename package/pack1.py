def duplication(l):
    l1=[]
    for i in l:
        if (i not in l1):
            l1.append(i)
    print(l1)


def unique(l):
    l1=[]
    for i in l:
        if l.count(i)==l:
            l1.append(i)
    print(l1)
