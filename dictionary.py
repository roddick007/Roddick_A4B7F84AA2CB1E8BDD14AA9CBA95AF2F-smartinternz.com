def add(myDict):
    values = []
    for i in myDict:
        values.append(myDict[i])
    final = sum(values)
    return final

my_dict = {'a': 600, 'b': 400, 'c': 700}

print("Sum:", add(my_dict))
