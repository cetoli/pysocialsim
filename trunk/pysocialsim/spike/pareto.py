from random import random, paretovariate, weibullvariate, uniform

alpha = 1.8
k = 1073741824
s0_1 = 0
s1_2 = 0
s2_3 = 0
s3_4 = 0
s4_5 = 0
for i in (range(1000)):
    t = k/pow(uniform(0,1), 1/alpha)
    print t
    
