# To calculate entered number is even or odd.
#   #   #   #   #   #   #   #   #   #   
#   Even number is divisible by 2.  #
#   * 0 is also an Even number.     #
#   #   #   #   #   #   #   #   #   #   
num = int(input('Enter a Natural Number: '))

if(num%2 == 0):
    print(num,'is an Even Number.')
else:
    print(num,'is an Odd Number.')