#Create a program that ask user to input 10 numbers. Print how many are even numbers.
evenum = 0
for i in range(10):
    a = int(input("Enter Number: "))
    if a % 2 == 0:
        evenum += 1
print(evenum)