# Control Flow
# if, elif, else

# if Condition: 
   # Do this

# if (agr sujeet sham m milega):
#     toh chai peena hai


# num = 15

# if num > 10 and num < 20:
#     print("Number is between 10 and 20")
#     print (f" The number was {num}")


# if num < 10 or num > 20:
#     print("Number is between 10 and 20")
#     print (f" The number was {num}")
# elif num == 15:
#     print(" Mast result hai bhai")
# else :
#     print(f" The number was {num}")


# example of not:
# not + True = False
# not + false = True

# logged_in = False
# if not logged_in:
#     print("Please log in first!")



# Nested conditions

# age = int(input("Enter age: "))
# citizen=True

# if age >= 18:
#     if citizen == input("Check for 'True' or 'False': "):
#         print("You are eligible to vote.")
#     else:
#         print("You must be a citizen to vote.")
# else:
#     print("You are not old enough to vote.")



# Loops (for, while)

# default value of range(start=0, stop=can change, step=1)

# numbers = list(range(10))
# print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# numbers = list(range(2,10))
# print(numbers)
# [2, 3, 4, 5, 6, 7, 8, 9]

# numbers = list(range(10,2))
# print(numbers)
# [10, 9, 8, 7, 6, 5, 4, 3]

# numbers = list(range(10,2,-2))
# print(numbers)
# [10, 8, 6, 4]

# numbers = list(range(10,2,2))
# print(numbers)

# Loop control (break, continue, pass)


# task --> 15  | output== 1,3,5,7,9,11,13,15

count=0
flag= True
# while flag:
#    count+=1
#    if count%2 != 0:
#       print(count)
#    if count > 15:
#       flag = False

# =======================================================

# for i in range(1,16):
#     if i%2 != 0:
#         print(i)


# for loop --> 
# for var in list/range/len(string)/len(list):
#    print("do this mutiple time")


# list= []
# range(start, end, step)
# len

# a = "Atul"
# b= "Solanki"

# print(len(a))
# print(len(b))

# =======================================================
# For loop using the String
# name="Atul"

# for i in name:
#    print(i)

# =======================================================
# For loop using the list

# list_of_names= ['Prateek','Sujeet','Akash']

# for name in list_of_names:
#     print(name)


# =======================================================
# For example 

# list1=[1,3,7,13,15,2,"m","kon"]

# for i in list1:
#    if i ==15: 
#       print("Mil gaya bhai : 15")
#    else: 
#       print(i) 
   


