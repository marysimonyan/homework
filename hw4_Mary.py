"""
Homework
Mary Simonyan
"""

"""
Problem 1
"""
# s1 = "Environment"
# s2 = "Earth"
#
# new = s1[:6] + s2 + s1[6:]
# print(new)


"""
Problem 2
"""
# s1 = "qwerty"
# s2 = "asdfg"
# s3 = "tyu"
# s4 = "1234"
# s5 = "p"
#
# n1 = s1[:1] + s2[:1] + s3[:1] + s4[:1] + s5[:1]
# n2 = s1[5:] + s2[4:] + s3[2:] + s4[3:] + s5[0:]
#
# print(n1, n2)

"""
Problem 3
"""

# name = input("Enter a name: ")
# if len(name) % 2 == 0:
#     print(name)
# else:
#     print(name.upper())

"""
Problem 4
"""
article = """ (CNN)The University of Virginia has disenrolled 238 students for its fall semester on Friday for not 
complying with the university's Covid-19 vaccine mandate, according to a university spokesperson.
UVA requires "all students who live, learn, or work in person at the university" to be fully vaccinated 
for the upcoming 2021-2022 academic year, according to current university Covid-19 policies.
Out of the 238 incoming Fall semester students, only 49 of them were actually enrolled in classes, and the remaining 
189 "may not have been planning to return to the university this fall at all," UVA spokesperson Brian Coy told CNN.
"Disenrolled means you're not eligible to take courses," Coy said. 
He added that students who were enrolled at the university on Wednesday still have a week to update their status 
at which point they can re-enroll.
"""

# print(article.count("university"))
# print(article.count("vaccine"))
# if article.count("student") % 2 == 0:
#     print(0)
# else:
#     print(article.count("student"))
#
#
# # 2nd version
# print(article.count('university') + article.count('University'))
# print(article.count('student') - article.count('students'))
# print(article.count('vaccine'))


"""
Problem 5
"""
# if article.find("2021-2022"):
#     print(article.split("2021-2022"))
#
# # example 2
# print(article.find('2021-2022'))
# print(article.index())
# print(article[323:332])
"""
Problem 6
"""
# sentence = "The quick brown fox jumps over the lazy dog"
# print(sentence[:19] + sentence.upper()[19:])
#
#
# def half_upper(str1):
#     half_length = len(str1) // 2
#     return str1[:half_length] + str1[half_length:].upper()
#
#
# print(half_upper("mary"))

"""
Problem 7
"""
# name = "Mary Simonyan"
# job = "programmer"
#
# print(f"I am", name, "and I am a", job, ".")

"""
Problem 8
"""
# number = str(input("Enter a number: "))
# print("The reversed version of the number is: ", number[::-1])
#
#
# # version 2
# def reverse(number):
#     num = str(number)
#     return num[::-1]
#
#
# print(reverse(876))
#
# # version 3
# def reverse(num_str):
#     n1 = num_str[-1]
#     n2 = num_str[1]
#     n3 = num_str[]
#
#
#
# print(reverse("987"))
