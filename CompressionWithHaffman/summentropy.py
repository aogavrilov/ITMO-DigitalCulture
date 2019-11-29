import math
mm=[0.0078125,0.0078125,0.0078125,0.03125,0.296875,0.6484375]
summentropy = 0;
for x in mm:
    summentropy-=x*math.log2(x)
    print(x*math.log2(x))
print(summentropy)