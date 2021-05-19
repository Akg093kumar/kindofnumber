# Perfect Number

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # 
#  Perfect number is a number which is equals to sum of its positive factors (excluding itself).            #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   

num = int(input('Enter a Natural Number: '))
s=0 #sum
for x in range(1,num):
    if((num % x) == 0):
        s += x

if s == num:
    print(num,'is a Perfect Number')
else:
    print(num,'is not a Perfect Number')

