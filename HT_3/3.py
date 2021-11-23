#Task 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
#яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
month = int(input("Enter a month: "))
def season(month):
    if (month == 12 or 0 <= month <= 2):
        return "winter"
    elif (3 <= month <= 4):
        return "spring"
    elif (5 <= month <= 8):
        return "summer"
    elif (9 <= month <= 12):
        return "autumn"
print(season(month))