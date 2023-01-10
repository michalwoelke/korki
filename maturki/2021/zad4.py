def main():
	arr = [[y for y in x.split(' ')] for x in open('Dane_2105/instrukcje.txt', 'r').read().strip().split('\n')]
	# print(arr)
	print(napis(arr))
	# napis = 'ZLAMTURHNG'
	# indx = int(napis.find('A'))
	# print(indx)
	# # print(napis[0:])
	# split_l = napis[:indx]
	# split_r = napis[indx + 1:]
	# print(split_l)
	# print(split_r)


def napis(arr:list):
	napis = ''
	dopisywane_litery = []
	for i in range(len(arr)):
		if arr[i][0] == 'DOPISZ':
			dopisywane_litery.append(arr[i][1])
			napis += arr[i][1]
		elif arr[i][0] == 'ZMIEN':
			napis = napis[:-1] + arr[i][1]
		elif arr[i][0] == 'USUN':
			napis = napis[:-1]
		else:
			indx = int(napis.find(arr[i][1]))
			split_l = napis[:indx]
			split_r = napis[indx + 1:]
			if arr[i][1] == 'Z':
				napis = split_l + 'A' + split_r
			else:
				napis = split_l + chr(ord(arr[i][1])+ 1) + split_r
	highest_count = 0
	highest_count_letter = ''
	for el in dopisywane_litery:
		if dopisywane_litery.count(el) > highest_count:
			highest_count_letter = el
			highest_count = dopisywane_litery.count(el)
	aktualna_seria = 0
	najdluzsza_seria = 0
	polecenie_seryjne = ''
	for i in range(len(arr) - 1):
		if arr[i][0] == arr[i + 1][0]:
			aktualna_seria += 1
			if aktualna_seria > najdluzsza_seria:
				najdluzsza_seria = aktualna_seria
				polecenie_seryjne = arr[i][0]
		else:
			aktualna_seria = 0

	return f'końcowy napis to: {napis}, a jego długość to {len(napis)}, najczęściej dopisywana litera to: {highest_count_letter} i występuje: {highest_count} razy, najdłuższa seria to: {najdluzsza_seria + 1} dla polecenia: {polecenie_seryjne}'



if __name__ == '__main__':
	main()
