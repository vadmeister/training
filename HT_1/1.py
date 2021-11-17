#Task 1 Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple
numbers = input("Enter numbers separated by a comma: ")
x = numbers.split(", ")
y = tuple(x)
print(x)
print(y)