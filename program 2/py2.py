def Count():
    NumList = []
    num = int(input("Enter the number of elements: ")) 
    for i in range(0, num): 
        elements = int(input("Enter the numbers: ")) 
        NumList.append(elements)
    search = int(input("Enter the number to count: "))
    count = 0
    for i in range (0, num):
        if(search == NumList[i]):
            count = count + 1
    print(search , " occured ", count, " times")
Count()
# eppai tha varutu 