#Task8. Написати скрипт, який отримує від користувача позитивне ціле число і створює словник
#з ключами від 0 до введеного числа, а значення для цих ключів - це квадрат ключа.
num = int(input("Any positive number here: "))
dictionary=dict()
for x in range(0,num+1):
    dictionary[x]=x**2
print(dictionary)
