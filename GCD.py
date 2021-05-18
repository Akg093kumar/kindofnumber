# Find out the Greatest Common Divisor(GCD) | Highest Common Factor(HCF) of given integers

import math

#let store all integers(to be calculated for their gcd) inside a list

gcd_num=[]
size=int(input('Size of list = '))
print('Enter ', size, ' integers for GCD calculation:')
for i in range(size):
    gcd_num.append(int(input()))
print(gcd_num)  #to check integers are listed or not

#if only single integer is there, then it's gcd is number itself 
if size == 1:
    print('gcd = ',gcd_num[0])
    exit
elif size>1:

    n1=gcd_num[0]
    n2=gcd_num[1]
    gcd=math.gcd(n1,n2)

    for i in range(2,len(gcd_num)):
        gcd=math.gcd(gcd,gcd_num[i])

    print('gcd of ', gcd_num ,' = ',gcd)




# GCD for two integers
# ----------------------
#a=int(input("Enter a positive integers:\n"))
#b=int(input("Enter a positive integers:\n"))
# a,b=map(int,input("Enter two positive integers:\n").split())

# def gcd(a,b):
#     if((b==0)|(b==a)):  
#         return a
#     elif(a==0):
#         return b
#     else:
#         return gcd(b,a%b)
# g=gcd(a,b)
# print("gcd(%d,%d)= " % (a,b), g)

