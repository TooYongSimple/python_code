import random

def get_200_number():
	L = []
	while True:
		f = random.randint(100000, 999999)
		if f in L:
			pass
		else:
			L.append(f)

		if len(L) == 200:
			break

	L.sort()
	return L


print get_200_number()
