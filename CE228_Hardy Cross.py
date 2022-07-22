# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:17:24 2022

@author: Admin
"""

from random import uniform
Q = float(input("Enter the value of Q (Q>Qo):")) #Input
Qo = float(input("Enter the value of Qo:")) #Output at branch
r=[0,0,0,0,0]
#Enter r values (integral)
r[0] = int(input("Enter (integral) r value for pipe 1:"))
r[1] = int(input("Enter (integral) r value for pipe 2:"))
r[2] = int(input("Enter (integral) r value for pipe 3:"))
r[3] = int(input("Enter (integral) r value for pipe 4:"))
r[4] = int(input("Enter (integral) r value for pipe 5:"))
n = 2 #Assumed
Q1 = uniform(Qo,Q) 
Q2 = Q - Q1
Q3 = uniform(1,Q1-Qo-1)
Q4 = Q1 - Qo - Q3
Q5 = Q2 + Q3
Q_arr = [Q1,Q2,Q3,Q4,Q5]
del1 = 0.5 #Assumed initial value of delta 1 
del2 = 0.5 #Assumed initial value of delta 2
sgn = 1
iterations = 1
print("Assumed inital flow values respectively:")
print(Q_arr)
while(abs(del1)>1e-5 and abs(del2)>1e-5):
 num1 = r[0]*(Q_arr[0]**n) - r[1]*(Q_arr[1]**n) + r[2]*(Q_arr[2]**n)*sgn
 dem1 = abs(r[0]*n*(Q_arr[0]**(n-1))) + abs(r[1]*n*(Q_arr[1]**(n-1))) + abs(r[2]*n*(Q_arr[2]**(n-1)))
 del1 = -num1/dem1 #loop 1
 Q_arr[0] = Q_arr[0] + del1
 Q_arr[1] = Q_arr[1] - del1
 Q_arr[2] = Q_arr[2] + del1*sgn
 if(Q_arr[2]<0):
     sgn = -1
 else:
     sgn = 1
 num2 = -sgn*r[2]*(Q_arr[2]**n) + r[3]*(Q_arr[3]**n) - r[4]*(Q_arr[4]**n)
 dem2 = abs(r[2]*n*(Q_arr[2]**(n-1))) + abs(r[3]*n*(Q_arr[3]**(n-1))) + abs(r[4]*n*(Q_arr[4]**(n-1)))
 del2 = -num2/dem2 #loop 2
 Q_arr[2] = Q_arr[2] - del2*sgn
 Q_arr[3] = Q_arr[3] + del2
 Q_arr[4] = Q_arr[4] - del2
 if(Q_arr[2]<0):
     sgn = -1
 else:
     sgn = 1
 print("Iteration: ",iterations)
 print("Flow values:",Q_arr)
 print("Delta Q for loop 1: ",del1)
 print("Delta Q for loop 2: ",del2)
 iterations+=1
print("Final Result: ")
print("Pipe 1:",Q_arr[0],"m3/s")
print("Pipe 2:",Q_arr[1],"m3/s")
print("Pipe 3:",Q_arr[2],"m3/s")
print("Pipe 4:",Q_arr[3],"m3/s")
print("Pipe 5:",Q_arr[4],"m3/s")
print("Delta Q1:",del1)
print("Delta Q2:",del2)
print("Iterations:",(iterations-1))
