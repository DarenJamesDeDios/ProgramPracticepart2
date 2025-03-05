# Create a program that ask user to input 2 numbers. Print the smaller number 
first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))

if first > second:
    print(f'{second} is the smaller number')
else:
    print (f'{first} is the smaller number')
