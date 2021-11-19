#Task7. Написати скрипт, який отримає максимальне і мінімальне значення із словника
dictionary = {"recre": 34, "ytrac": 23, "4": 46}
min_key = min(dictionary, key=dictionary.get)
max_key = max(dictionary, key=dictionary.get)
print ('Min: ', dictionary.get(min_key))
print ('Max: ', dictionary.get(max_key))
