from random import uniform
import math

lambd = 40.0
k = 0.59
x0 = 0
s0_1 = 0
s1_2 = 0
s2_3 = 0
s3_4 = 0
s4_5 = 0
arq = open("distWeibull.log", 'w')
line = ""
#print "Menor: ", lambd*pow((-math.log(0.12)), 1/k)
#print "Maior: ", lambd*pow((-math.log(0.99)), 1/k)
#print "----------------------------------------"
for i in range(1, 1000):
    t = lambd*pow((-math.log(uniform(0,1))), 1/k)#math.exp(-pow((i - x0)/lambd, k))
    print t  #lambd*pow((-math.log(uniform(0,1))), 1/k)*
    line += str(t) + "\n"
    x0 += t
    

arq.write(line)
arq.close()
print "media", x0/(1000)