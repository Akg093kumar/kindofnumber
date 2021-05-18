#Python program to find the factorial of a number provided by the user.
n=int(input("Number="))

def facto(n):
    if(n<0):
        print("Please insert an positive integer and Try again!!!")
    elif((n==0)|(n==1)):
        return 1
    else:
        return facto(n-1)*n

print(n,"! = ",facto(n)) 