def String_Functions():
    str = "Hello World"
    print("String: ", str)
    print("1. Number of letters: ", len(str))
    print("2. Replace of World: ", str.replace("World", "Welcome"))
    print("3. Isalpahanumeric: ", str.isalnum())
    print("4. Center Alignment: ", str.center(20))
    print("5. Index of W: ", str.find('W'))
    print("6. ToUpper: ", str.upper())
    print("7. StartsWith H: ", str.startswith('H'))
    print("8. Count of o: ", str.count('o'))
    print("9. Split: ", str.split(' '))
    print("10. Partition: ", str.partition(' '))
    print("11. Last Index of o: ", str.rindex('o'))
    print("12. Zfill: ", str.zfill(15))
    print("13. IsTitle: ", str.istitle())
String_Functions()