def dik(dict1):
    list1 = []
    for k,v in dict1.items():
        list1.append(k)
        list1.append(v)
    return list1

dict1 = { "a": 1, "b": 2 }
print(dik(dict1))
