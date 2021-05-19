# To check entered number is prime or composite
#   #   #   #   #   #   #   #   #   #   #   #   #
#   Prime number is divided by 1 and itself.    #
#   Thus it has only two factors                #
#   #   #   #   #   #   #   #   #   #   #   #   #
num = int(input('Enter an positive integer: '))
c=0
if num<0:
    print('Sorry. Enter an Positive integer to proceed.')
    exit
elif(num>0):
    for i in range(2,num):
            if(num%i == 0):
                c+=1
    #print(c)
    if(c == 0):
        print(num,'is Prime number')
    else:
        print(num,'is a Composite Number')
