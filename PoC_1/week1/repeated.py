def appendsum(lst):
    """
    Repeatedly append the sum of the current last  3 elemtns to lst
    """
    for i in range(25):
        lst.append(lst[-1]+lst[-2]+lst[-3])

ls=[0,1,2]
appendsum(ls)

print(ls[10])
print(ls[20])
