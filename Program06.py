#Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers
numbers = [float(input("Enter number: ")) for i in range(10)]
print(numbers[0] - sum(numbers[1:]))

