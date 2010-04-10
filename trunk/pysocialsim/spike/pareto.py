from random import random, paretovariate, weibullvariate, uniform

alpha = 0.2
beta = 2
k = 900
s0_1 = 0
s1_2 = 0
s2_3 = 0
s3_4 = 0
s4_5 = 0
for i in (range(24445*2)):
    t = k/pow(uniform(0,1), 1/alpha)
    messagesLogFile = open("teste.log", "a")
    line = str(t) 
    messagesLogFile.write(str(line)+"\n")
    messagesLogFile.close()
    print t
    
