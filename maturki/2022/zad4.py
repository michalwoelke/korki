def main():
	arr = [x for x in open('Dane_2205/liczby.txt', 'r').read().strip().split('\n')]
#	answers:
#	zad1: (18, 93639)
#	zad2: (99792, 10), (62790, 6)
#	zad3: odp wyprintowana
	# print(arr)
	# print(zad1(arr))
	print(zad3(arr))


def zad1(arr:list):
	how_many = 0
	highest = 0
	for el in arr:
		if el[0] == el[-1]:
			how_many += 1
			if highest == 0:
				highest = int(el)
	return how_many, highest


def zad2(arr:list):
	arr = [int(x) for x in arr]
	all_czynniki = []
	most_czynniki = 0
	number_of_1 = 0
	most_unique_czynniki = 0
	number_of_2 = 0
	for el in arr:
		czynniki = []
		k = 2
		tmp = el
		while el != 1:
			while el % k == 0:
				el //= k
				czynniki.append(k)
			k += 1
		if len(czynniki) > number_of_1:
			most_czynniki = tmp
			number_of_1 = len(czynniki)
		if len(set(czynniki)) > number_of_2:
			most_unique_czynniki = tmp
			number_of_2 = len(set(czynniki))
	return (most_czynniki, number_of_1), (most_unique_czynniki, number_of_2)


def zad3(arr:list):
	arr = [int(x) for x in arr]
	trojki = []
	for x in arr:
		for y in arr:
			if y != x:
				if y % x == 0:
					for z in arr:
						if z != y and z != x:
							if z % y == 0:
								trojka = []
								trojka.append(x)
								trojka.append(y)
								trojka.append(z)
								trojki.append(trojka)
	out_trojki = [tuple(x) for x in trojki]
	piatki = []
	for u in arr:
		for w in arr:
			if w != u:
				if w % u == 0:
					numbers = [u,w]
					for x in arr:
						if x not in numbers:
							if x % w == 0:
								numbers = [u,w,x]
								for y in arr:
									if y not in numbers:
										if y % x == 0:
											numbers = [u,w,x,y]
											for z in arr:
												if z not in numbers:
													if z % y == 0:
														piatka = [u,w,x,y,z]
														piatki.append(piatka)
	out_piatki = [tuple(x) for x in piatki]
	return f'dobrych trójek jest: {len(trojki)} i są to {out_trojki} a dobrych piatek jest {len(piatki)} i sa to {out_piatki}'


if __name__ == '__main__':
	main()
