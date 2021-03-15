def polynomial():
    import math
    print("Enter the coefficients of the form ax^3 + bx^2 + cx + d")
    lst = []
    for i in range(0,4):
        co =int(input("Enter the coefficient: "))
        lst.append(co)
    x = int(input("Enter the value of x: "))
    sum = 0
    j = 3
    for i in range(0,3):
        while(j > 0):
            sum = sum + (lst[i] * math.pow(x,j))
            break
        j = j - 1
    sum = sum + lst[3]
    print("The value of the polynomial is:", sum)
polynomial()