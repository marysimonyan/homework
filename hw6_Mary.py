"""
Homework 6
Mary
"""

import os

"""
Problem 1
"""
# f = open(r"C:\Users\Mary Simonyan\Desktop\file.txt", "w")
# f.write("My favorite fruits are: \n")
# f = open(r"C:\Users\Mary Simonyan\Desktop\file.txt", "a")
# f.write("mango\nwatermelon\nraspberry\npineapple\nfig\n")

"""
Problem 2
"""
# file = open(r"C:\Users\Mary Simonyan\Desktop\file1.txt", "w")
# file.write("hello\nhow\nare\nyou\ndoing")
# file = open(r"C:\Users\Mary Simonyan\Desktop\file1.txt", "r")
#
# var1 = file.readline()
# var2 = file.readline()
# var3 = file.readline()
# var4 = file.readline()
# var5 = file.readline()
# file.close()
#
#
# print(var1, var2, var3, var4, var5, end='\r')
"""
Problem 3
"""
# file = open(r"C:\Users\Mary Simonyan\Desktop\file2.txt", "r")
# file.write("""On offering to help the blind man, the man who then stole his car, had not, at that precise moment,
# had any evil intention, quite the contrary, what he did was nothing more than obey those feelings of generosity and
# altruism which, as everyone knows, are the two best traits of human nature and to be found in much more hardened
# criminals than this one, a simple car-thief without any hope of advancing in his profession, exploited by the real
# owners of this enterprise, for it is they who take advantage of the needs of the poor.""")

# # found the code from the internet and changed it a bit
# with open(r"C:\Users\Mary Simonyan\Desktop\file2.txt") as file:
#     data = file.read().split()
#     maxi = len(max(data, key=len))
#     res = [word for word in data if len(word) == maxi]
#     print(res)

# # version 2
# f = file.read().replace(',', '').replace('.', '')
# # print(f)
# word_list = f.split()
# # print(word_list)
# longest_word = ''
# for word in word_list:
#     if len(word) > len(longest_word):
#         longest_word = word
# print(longest_word)

"""
Problem 4
(incomplete)
"""
# ls = ["Mary", "Ani"]
#
# for i in ls:
#     f = open(rf"C:\Users\Mary Simonyan\Desktop\{i}.txt", "w")
#     f.write(f"{i}\n" * len(i) + "\n")
#
# version 2
# for name in ls:
#     f = open()

"""
Problem 5
!
"""
# new_names = ['Ani', 'Armen', 'Aren', 'Argishti', 'Arsen', 'Alik', 'Anahit', 'Anna']
#
#
# def check(ls):
#     for i in ls:
#         if os.path.exists(rf"C:\Users\Mary Simonyan\Desktop\{i}.txt"):
#             return True
#         else:
#             return False

"""
Problem 6
"""
# file = open(r"C:\Users\Mary Simonyan\Desktop\file.txt", "r")
#
#
# word = str(file)
# import re  # couldn't figure out how to make isupper() work, so i found this method on the internet
#
# patterns = ['[A-Z]+']
#
# for p in patterns:
#     match = re.findall(p, word)
#     print(match)
#
# # Version 2
# def up(file):
#     n = 0
#     f = file.read()
#     for char in f:
#         if char.isupper():
#             n += 1
#     return n
#
#
# with open(r"C:\Users\Mary Simonyan\Desktop\file.txt") as file:
#     print(up(file))

"""
Problem 7
"""
# file = open(r"C:\Users\Mary Simonyan\Desktop\file.txt", 'r')
# word_list = file.read.replace(',', '').split()
# unique_words = set(word_list)
# for word in unique_words:
#     print(f'frequency of "{word}" is: ', word_list.count(word))

