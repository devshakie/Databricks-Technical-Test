# Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.

def reverse_integer(num):
    sign = -1 if num < 0 else 1   
    reversed_num = int(str(abs(num))[::-1])
    return sign * reversed_num

print(reverse_integer(500))
print(reverse_integer(-56))
print(reverse_integer(-90))
print(reverse_integer(91))
    
    
