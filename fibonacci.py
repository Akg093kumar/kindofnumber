# Program to display the Fibonacci sequence up to n-th term
num=int(input("Enter size of fibonacci series: \n"))

def fibo(n):
   
    if n<=1:
        return n
    else:
        return (fibo(n-2)+fibo(n-1))

if(num<=0):
    print(" :( *Enter positive integer value as size. Try again!!!* ")
else:
    print("Fibonacci Series:")
    for i in range(num):
        print(fibo(i),end=" ")