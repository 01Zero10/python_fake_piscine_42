import sys

states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
}
capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver",
	"DB": "Denver"
}

if len(sys.argv) != 2:
	for element in capital_cities.items():
		if element[1] != sys.argv[1]:
			continue
		for ele in states.items():
			if ele[1] != element[0]:
				continue
			print(ele[0])
			break
		break

		
		