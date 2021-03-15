def CountChar():
    str=input("Enter the string: ")
    dictionary = {} 
    for i in str: 
        if i in dictionary: 
            dictionary[i] += 1
        else: 
            dictionary[i] = 1
    print("Dictionary:", dictionary)
CountChar()
