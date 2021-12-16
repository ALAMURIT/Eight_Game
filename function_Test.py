x = [1, 2, 3, 4, 5, 6]
y = []
def equalList(list_1, list_2):
    for element in list_1:
        list_2.append(element)
    return(list_2)

equalList(x, y)
def swap(x, i, j):
    x[i], x[i + 1] = x[i + 1], x[i]
    return(x)
swap(y, 0, 0)
print(x)
print(y)
z = []
for i in range(0, 9, 1):
    j = i
    z.append(j)
print(z)