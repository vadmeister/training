#Task2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення
num = int(input("The value to which the last element of the tuple is replaced: "))
x = [(10, 20, num), (30, 40, 50, num), (60, 70, 80, 90, num)]
print (x)
print([t[:-1] + (100,) for t in x])
