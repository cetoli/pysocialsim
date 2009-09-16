from random import uniform
import math

lambd = 13.7007
k = 3.9867
x0 = 0

s0_1 = 0
s1_2 = 0
s2_3 = 0
s3_4 = 0
s4_5 = 0
arq = open("teste.txt", 'w')
line = ""
#print "Menor: ", lambd*pow((-math.log(0.12)), 1/k)
#print "Maior: ", lambd*pow((-math.log(0.99)), 1/k)
#print "----------------------------------------"
for i in range(1, 1000):
    t = lambd*pow((-math.log(uniform(0,1))), 1/k)#math.exp(-pow((i - x0)/lambd, k))
    print t  #lambd*pow((-math.log(uniform(0,1))), 1/k)*
    line += str(t).replace(".", ",") + "\n"
    
    if t < 1:
        s0_1 += 1
    elif t >= 1 and t < 2:
        s1_2 += 1
    elif t >= 2 and t < 3:
        s2_3 += 1
    elif t >= 3 and t < 4:
        s3_4 += 1

arq.write(line)
arq.close()
print (s0_1/302401.0)*100
print (s1_2/302401.0)*100
print (s2_3/302401.0)*100
print (s3_4/302401.0)*100