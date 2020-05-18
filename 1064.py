a, b, c = input().split()
x = int(a)
y = int(b)
z = int(c)
cmpr_xy = x if x < y else y
print(cmpr_xy if cmpr_xy < z else z)
