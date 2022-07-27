from multiprocessing.sharedctypes import Value


data = {}

data1 = [1,2,3,4,5]

value = [9,8,3,5]

for i in data1:
    for j in value:
        data.setdefault(i,[]).append(j)

print(data)
