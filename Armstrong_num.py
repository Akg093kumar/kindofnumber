# Python program to check if the number is an Armstrong number or not

num = int(input("Enter an integer: "))
tmp = num
sum = 0

c1 = str(num)   #convert to string to find length 
c = len(c1)     #counts no of digits in the entered number
c2 = int(c1)    #re-convert to integer for further calculations

r = 0           #remainder

while tmp != 0:
    r = tmp % 10
    sum = sum + pow(r,c)
    tmp = tmp // 10

if(sum == num):
    print(num,"is  an Armstrong Number.")
else:
    print(num,"is not an Armstrong Number.")



#code is contributed by Asish Kumar Gouda
