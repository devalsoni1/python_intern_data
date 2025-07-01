# name = input("enter student name")
# clas = input("input class of student")

# mark1=int(input("mark of subject"))
# mark2=int(input("mark of subject"))
# mark3=int(input("mark of subject"))
# mark4=int(input("mark of subject"))
# mark5=int(input("mark of subject"))

# tm = mark1 + mark2 + mark3 +mark4+mark5

# print("Total marks is : ",tm)

# per = (tm / 5* 100 )

# print("percentage is : ",per)

# s1 = input("enter a line 1")

# s2 = input("enter line 2")

# s = s1+s2

# print(s)

# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.swapcase())
# print(s.capitalize())
# print(s.casefold())
# # print(s.center())
# # print(s.count())
# print(s.endswith())
# print(s.find())
# print(s.isalnum())
# print(s.isdigit())
# print(s.isspace())
# print(s.replace())

mark1=int(input("mark of subject : "))
mark2=int(input("mark of subject : "))
mark3=int(input("mark of subject : "))
mark4=int(input("mark of subject : "))
mark5=int(input("mark of subject : "))

tm = mark1 + mark2 + mark3 +mark4+mark5

print("Total marks is : ",tm)

per = (tm / 500) *100

if per >= 60:
    grade = 'A'

elif per >=50 and per <=60:
    grade = 'B'

elif per >= 40 and per <= 50:
    grade = 'C'

else:
    grade = 'Faail'

print(f"Grade : {grade}")
