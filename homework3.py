#making calculator#

a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))

print("1.Add \n2.Subtract \n3.Multiplication \n4.Division ")
c=input("Enter what operation you want to be done: ")

if c == '1':
    print(a,"+",b,"=",float(a)+float(b))

elif c == '2':
    print(a,"-",b,"=", float(a) - float(b))

elif c == '3':
    print(a,"*",b,"=",float(a) * float(b))

elif c == '4':
    print(a,"/",b,"=",float(a)/float(b))

else:
    print("Invalid Input.")

#checking loop year#

year = int(input("Enter the year you want to check as a leap year: "))
if year % 4 == 0 and year % 100 != 0:
    print(" The year ",year," is a leap year.")
else:
    print(" Sorry, the year ",year," is not a leap year.")

#Asking user's information#

name = input("Enter your name: ")
if name.isalpha() == True:
    print("Valid Username")
else:
    print("Invalid Username")

age = (input("Enter your age: "))
if age.isnumeric() == True and int(age)>18:
    print("Valid age")
else:
    print("Invalid age")

num = (input("Enter your mobile number: "))
if num.isdigit() == True:
    print("Valid mobile number")
else:
    print("Invalid mobile number")


#dimensions and polygon#

len1 = int(input("Enter the first length: "))
len2 = int(input("Enter the second length: "))
brd1 = int(input("Enter the first breadth: "))
brd2 = int(input("Enter the second breadth: "))

if len1 == len2 == brd1 == brd2:
    print("It is a square.")
elif len1 == len2 or brd1 == brd2:
    print("It is a rectangle.")
else:
    print("It is neither square nor rectangle.")


#this much for class 4#