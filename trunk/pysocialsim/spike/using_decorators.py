import math

l = 1/3600.0
k = l
x = 28800
s = 0
for i in range(1, 9):
    
    v = ((k*pow(x, k - 1))/pow(l, 2))*(math.exp(-pow(x/l, l)))
    print x, v*100
    x -= 3600.0
    s += v
    
print s*100
