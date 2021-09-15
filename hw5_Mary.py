"""
Homework 5
Mary Simonyan
"""

"""
Problem 1
"""
# ls = [5, 11, 30, 45, 175, 99, 106, 300, 490, 512, 890, 1000]
# index = 0
#
# while index < len(ls):
#     element = ls[index]
#     if element % 5 == 0:
#         print(element)
#     if element >= 500:
#         break
#     index += 1

"""
Problem 2
"""
# list1 = [1, 2, 3, 4, 5]
#
# for i in list1[::-1]:
#     print(i)

"""
Problem 3
"""
# num = int(input("enter a number: "))
# fac = 1
# for i in range(1, num + 1):
#     fac = fac * i
# print("factorial of ", num, " is ", fac)

"""
Problem 4
"""
# for loop
# list1 = [10, 11, 12, 13, 14, 15]
# for i in range(len(list1)):
#     if i % 2 == 0:
#         print(list1[i], end=", ")

# while loop


"""
Problem 5
"""
# names = [' Anna', "Lily", " Anahit ", "@Bob", "@Ani@", " Luiza@", "@@Armen"]
#
# for name in names:
#     name = name.strip()
#     name = name.strip("@")
#     if name[0] == "A":
#         print(name)


"""
Problem 6
(not working)
"""
num = int(input("Enter a number: "))

for i in range(2, num):
    if (num % i) == 0:
        print(num, "is not a prime number.")
        break
else:
        print(num, "is a prime number.")

"""
Problem 7
"""
# n = 6
# for i in range(0, n):
#     for j in range(0, i):
#         print("* ", end="")
#     print("\r")
#
# # version 2
# for x in range(0, 6):
#     print(x * "* ")
#
# x = 0
# y = "*"
# while x
