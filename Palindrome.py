# To check entered input is Palindrome or not
#It can check for both string and integer input

#   #   #   #   #   #   #   #   #   #   
#   Plaindrome number is the number #
#   which is equal to its reverse   #
#   #   #   #   #   #   #   #   #   #   

pal = input('Enter ur input: ')
#pal_rev = pal[::-1]
if pal == pal[::-1]:
    print(pal,'is Palindrome.')
else:
    print(pal, 'is not a palindrome')


#Mathematical Approach
#-------------------------
# It can check only for positive integer input
# pal = int(input('Enter a number: '))
# t = pal # t is temporary variable
# s=0 #sum
# r=0 #remainder

# while(t != 0):
#     r = t % 10
#     s = (s * 10) + r
#     t = t//10
# if s == pal:
#     print(pal, 'is a palindrome number')
# else:
#     print(pal, 'is not a palindrome number')



