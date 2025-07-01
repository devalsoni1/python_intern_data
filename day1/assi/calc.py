no1 = int(input("enter 1st no. "))
no2 = int(input("enter 2st no. "))

add = no1 + no2
sub = no1 - no2
mul = no1 * no2
div = no1 / no2

choice = input("""
Enter your choice 
for Add +,
for Subtrate -,
for Multiply x,
for Divide / -- """)

if choice == "-":

    print(sub)

elif choice == "x":

    print(mul)

elif choice == "/":

    print(div)


elif choice == "+":

    print(add)

else:
    print("No response")