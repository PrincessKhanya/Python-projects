def great_int():

    list1=[]
    n=int(input("Input the lenth of the array you want: "))
    for y in range(n):
        y=int(input("enter the number for you array: "))
        list1.append(y)

    holder=list1[0]
    holder1=list1[0]

    for i in range(len(list1)):
        if list1[i]>holder:
            holder=list1[i]
        elif list1[i]<holder:
            holder=list1[i]
    print(holder)
    print(holder1)

great_int()