liczbaPowtorzen = 0

def przestaw(n):
	global liczbaPowtorzen
	r = n % 100
	a = r // 10
	b = r % 10
	n = n // 100
	w = 0
	if n > 0:
		w = a + 10 * b + 100 * przestaw(n)
	else:
		if a > 0:
			w = a + 10 * b
		else:
			w = b
	liczbaPowtorzen+=1
	return w

def przestaw2(n:int):
	strN = str(n)
	odpowiedz = ""
	iterator = 0
	if strl(strN) % 2 != 0:
		iterator = 1
		odpowiedz+=strN[0]
	while(iterator<strl(strN)):
		iterator+=1
		if (strl(strN) % 2 != 0 and iterator % 2 != 0) or (strl(strN) % 2 != 1 and iterator % 2 != 1):
			continue
		pomocy1 = strN[iterator]
		pomocy2 = strN[iterator-1]
		pomocy1, pomocy2 = pomocy2, pomocy1
		odpowiedz+=f"{pomocy2}{pomocy1}"
	return odpowiedz

	
def strl(text:str):
	result = 0
	for i in text:
		result+=1
	return result
	
zbiorN = [316498,43657688,154005710,998877665544321]
for n in zbiorN:
	print(n,przestaw2(n),liczbaPowtorzen)
	# przestaw2(n)
	# print(liczbaPowtorzen,len(f"{n}"))
	liczbaPowtorzen=0