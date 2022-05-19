

from tkinter import Y


d={
'Hendrix' : '1942', 'Allman' : '1946', 'King' : '1925', 'Clapton' : '1945', 'Johnson' : '1911', 'Berry' : '1926', 'Vaughan' : '1954', 'Cooder' : '1947', 'Page' : '1944', 'Richards' : '1943', 'Hammett' : '1962', 'Cobain' : '1967', 'Garcia' : '1942', 'Beck' : '1944', 'Santana' : '1947', 'Ramone' : '1948', 'White' : '1975', 'Frusciante': '1970', 'Thompson' : '1949', 'Burton' : '1939',
}

# year = []
# for e in list(d.values()):
# 	if e not in year:
# 		year.append(e)
# year.sort()

year = sorted(set(d.values()))

for yr in year:
	for element in d.items():
		if element[1] == yr:
			print(element[0])
print()
for yr in year:
	f = []
	for element in d.items():
		if element[1] == yr:
			f.append(element[0])
	f.sort()
	for name in f:
		print(name)









