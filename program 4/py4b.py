def DictMethod():
    Dictionary1 = dict({2: 'Zuckerbeg', 1: 'Steve', 3: 'Elon Musk'})
    Dictionary2 = {1: 'Steve Jobs'}
    print("Dictionary:", Dictionary1)
    Dictionary1.update(Dictionary2)
    print("Updated Dictionary:", Dictionary1)
    print("Sorted by Keys:", sorted(Dictionary1.keys()))
    print("Sorted by Values:", sorted(Dictionary1.values()))
    del Dictionary1[3]
    print("After removing key 3:", Dictionary1)
    cpy = Dictionary1.copy()
    print("After copying Dicionary1 to cpy:", cpy)
    cpy.clear()
    print("Clearing the Dictionary cpy:", cpy)
DictMethod()