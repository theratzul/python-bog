l = [2, 3, 4]
square = lambda x: x**2
newlist = map(square, l)
print(newlist)
double_list = list(map(square, l))
print(double_list)