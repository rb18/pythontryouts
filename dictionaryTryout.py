sozluk = {'key' : 'anahtar' , 'apple' : 'elma' , 'orange' : 'portakal'}

while(True):
	kelime = raw_input('Please enter a word to see it means in Turkish : ')
	if kelime in sozluk:
		print sozluk.get(kelime)
	else:
		kelime2=raw_input('Please enter the %s means in Turkish to append that dictionary :' % (kelime))
		sozluk[kelime] = kelime2
