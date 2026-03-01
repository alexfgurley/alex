# File name: homework4 

top_5_foods = ["pizza", "banh mi thit nuong", "bun bo", "burger", "bun thit nuong"]
# print second food in the list: 
#print(top_5_foods[2])

#print the last food using negative indexing: 
#print(top_5_foods[-1])

# add a new food to the list using .append(): 
top_5_foods.append("sushi")
#print(top_5_foods)

#insert "apple" at the start of the list: 
top_5_foods.insert(0, "apple")
#print(top_5_foods)

#remove the third item in the list using del or .remove()
top_5_foods.remove("banh mi thit nuong")
#print(top_5_foods)

#print length of the list with len
#print(len(top_5_foods))

#loop through thr list and print each food in uppercase(use .upper)
# i = 0
# for i in range(0,6) : 
#     str = top_5_foods[i] 
#     print(str.upper())
#     i += 1 

#create a new list containing only the first and last food(use slice)
first_and_last = [top_5_foods[0],top_5_foods[5]]
# print(first_and_last)

#use an if statement to check if potatoe is in the list. 
def check_potato(list) : 
    for i in range(0,6): 
        str = top_5_foods[i]
        for str in list : 
            if str == "potato" : 
                check_potato = "A potato!"
            else : 
                check_potato = "No potato!"
    return check_potato 
print(check_potato(top_5_foods))
top_5_foods.append("potato")
# print(check_potato(top_5_foods))

# 3.2 Slicing and Striding 
numbers = list(range(0,21))

# Step 1: 
def get_first_15(list) : 
    list[:] = [x for x in list if x < 16]
    return(list)
#print(get_first_15(numbers))

# Step 2: 
def get_every_5th(lst) : 
    lst[:] = [lst[x] for x in range(len(lst)) if x % 5 == 0]
    return(lst)
#print(get_every_5th(numbers))

# Step 3: 
def reverse_and_stride(lst) : 
    n = len(lst)
    reversed_lst = [None] * n
    for i in range(n) : 
        reversed_index = n - 1 - i
        reversed_lst[reversed_index] = lst[i] 
    print(f"The reversed list is {reversed_lst}")
    return reversed_lst[::3]
#print(reverse_and_stride(numbers))

# 3.3 Nested Lists 
# 3.3.1 Operations 
numbers = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print the 3rd row
#print(numbers[2])

# print the second item in the second row
# print(numbers[1][1])

# add a new row
numbers.append([10, 11, 12])
# print(numbers)

# write a function that loops through each row, sums all numbers returns the total
def sum_nested(nested_lst) : 
    total = 0
    i = 0
    for lst in nested_lst : 
        for i in range(len(lst)) : 
            total += lst[i]
    return total
# print(sum_nested(numbers)) 

# 3.4 Create a 5x5 list 
def create_nested_list(number) : 
    lst = []
    for i in range(1, number + 1, 5) : 
        sublst=[]
        for j in range(i, min(i+5,number + 1)) : 
            sublst.append(j)
        lst.append(sublst)
    return lst  
#print(create_nested_list(25))   

nested_list = create_nested_list(26)
     
def multiple_3(lst) : 
    for sublist in lst : 
        for i in range(len(sublist)): 
            if sublist[i] % 3 == 0 : 
                sublist[i] = "?"
    return lst
new_nested_list = (multiple_3(nested_list))
#print(new_nested_list)

def sum(lst) :
    sum = 0 
    for sublist in lst : 
        for i in range(len(sublist)) : 
            if sublist[i] != "?" : 
                sum += sublist[i]
    return sum 
#print(sum(new_nested_list))

# 4 Dictionaries 
# 4.1 Dictionary Operations 
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

# Print Katies age 
#print(ages["Katie"])

# Change Miras name to 100 
ages["Mira"] = 100
#print(ages)

# Add "milana" with age 52
ages["Milana"] = 52
#print(ages)

# Remove Mariam from dictionary 
del ages["Mariam"]
#print(ages)

# print each persons name and age
#for key in ages : 
#    print(key, ages[key]) 


my_list = [
[12, 47, 3, 19, 28],
[5, 34, 11, 22, 7],
[9, 16, 50, 2, 41],
[38, 14, 23, 46, 30]
]

n = sum_nested(my_list)
print(n)







