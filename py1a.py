def MaxMin():
    NumList = []
    num = int(input("Enter the number of elements: ")) 
    for i in range(0, num): 
        elements = int(input("Enter elements: ")) 
        NumList.append(elements)
        min = NumList[ 0 ]
    for a in NumList:
        if a < min:
            min = a
    print ("Minimum Number: ", min)
    max = NumList[0]
    for a in NumList:
        if a > max:
            max = a
    print("Maximum Number: ", max)
MaxMin()

    