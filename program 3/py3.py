#Linear Search:
def Linear():
    print("Linear Search:")
    def LinearSearch(NumList, n, Search):
        for i in range(0, n):  
            if (NumList[i] == Search):  
                return i  
        return -1   
    NumList = [1 ,2, 3, 4, 5]  
    print("Numbers: ", NumList)
    Search = int(input("Enter the number to be search: "))
    n = len(NumList)  
    Result = LinearSearch(NumList, n, Search)  
    if(Result == -1):  
        print("Element not found in a list")  
    else:  
        print("Element found at index: ", Result)  
Linear()


#Binary Search:
def Binary():
    print("Binary Search:")
    def BinarySearch(NumList, low, high, Search):
        if high >= low:
            mid = (high + low) // 2
            if NumList[mid] == Search:
                return mid
            elif NumList[mid] > Search:
                return BinarySearch(NumList, low, mid - 1, Search)
            else:
                return BinarySearch(NumList, mid + 1, high, Search)
        else:
            return -1
    NumList = [ 10, 20, 30, 40, 50 ]
    print("Number List: ", NumList)
    Search = int(input("Enter the number to be search: "))    
    result = BinarySearch(NumList, 0, len(NumList)-1, Search)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")
Binary()

