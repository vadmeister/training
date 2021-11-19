#Task5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями
dictionary = { 'red' : 122, 'theball' : 1643, 'forega' : 33, 'ornament' : 122, 'energy' : 755}
alt = []
result = dict()
for x, values in dictionary.items():
	if values not in alt:
		alt.append(values)
		result[x] = values
print(result)


