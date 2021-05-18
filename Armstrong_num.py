# Python program to check if the number is an Armstrong number or not

num = int(input("Enter an integer: "))
tmp = num
s = 0
c1 = str(num)   #convert to string to find length 
c = len(c1)
c2 = int(c1)    #re-convert to integer for further calculations
r = 0

while tmp != 0:
    r = tmp % 10
    s = s + pow(r,c)
    tmp = tmp // 10

if(s == num):
    print(num,"is  an Armstrong Number.")
else:
    print(num,"is not an Armstrong Number.")



