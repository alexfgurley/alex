# file: homework 3 

# --- Functions --- 
# 3.1
def say_goodbye(name) : 
    print(f"Goodbye {name}, have a nice day!")
# say_goodbye("Alex")

# 3.2 
pi = 3.14
def area_circle(R) : 
    print(pi * (R * R))
#area_circle(3)

# --- Return Functions --- 

# 4.1 
def subtract(a,b) : 
    return a - b
#print(subtract(10,1))

def multiply(a,b) : 
    return a * b
#print(multiply(1, 2)) 

def divide(a,b) : 
    if b == 0 : 
        return "Undefined"
    else : 
        return a / b
#print(divide(2, 0))

# --- conditionals --- 
# 5.1 

def min_max_temp(list) : 
    return min(list), max(list)
# print(min_max_temp([-1, 2, 3, 4, 100000]))

# 5.2 
# let each day of the week be represented by a number, monday = 1, tuesday = 2, ..., 
def check_weekend(num) : 
    if num == 6 or num == 7 : 
        return True
    else : 
        return False
# print(check_weekend(7))

# 5.3 
def fuel_e(miles, gallon) : 
    return miles / gallon

# 5.4 
def encryption_alg(integer) : 
    d = len(str(abs(integer)))
    e_1 = integer % 10
    e_2 = integer // 10 
    return (e_1 * (10 ** (d - 1)) + e_2)
# print(encryption_alg(12345))
# print(encryption_alg(5224375))

# --- Loops --- 
# 6.1 
def exponent(x,y) :  
    num = 1
    output = 1
    while num <= y : 
        output *= x
        num = num + 1
    return output
# print(exponent(2,0))

# 6.2 
# 6.2.1
def minimum(list1): 
    low = list1[0]
    for x in list1: 
        if x < list1[0]:
            low = x 
    return low 
# print(minimum([0,2,-1,2,100]))

def maximum(list1):
    max = list1[0]
    for x in list1: 
        if x > list1[0]:
            max = x 
    return max
# print(maximum([5,4,-2,3,4, 4 ** 2]))

# 6.2.2 
def min_while(list): 
    low = list[0]
    n = len(list)
    i = 1
    while i < n:
        if list[i] < low : 
            low = list[i]
        i += 1 
    return low  
# print(min_while([4,5,7,99,10000]))

def max_while(list): 
    high = list[0]
    n = len(list)
    i = 1 
    while i < n:
        if list[i] > high : 
            high = list[i]
        i += 1 
    return high
# print(max_while([1,2,3,4,5]))

# 6.3 
def integer_sum(integer): 
    i = 0
    n = len(str(integer))
    sum = 0 
    for i in range(n): 
        digit = (integer // (10 ** i) % 10)
        sum += digit
        i += 1 
    return sum 
# print(integer_sum(2468))

x = 123456
result = integer_sum(x) # the sum of all the digits of the integer x 
print(f"The result of Calculate the Sum (6.3) with x = {x} is {result}")

    
       
        
