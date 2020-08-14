def numerus(roman):
	roman_numerals={'i':1,'I':1,'v':5,'V':5,'X':10,'x':10,'L':50,'l':50,'c':100,'C':100,'m':1000,'M':1000,'d':500,'D':500}
	print(roman_numerals)
	total=0; prev=0
	for l in roman:
		cur=roman_numerals[l]
		if prev < cur:
			total -= prev
			cur -=prev
		total += cur
		prev=cur
	return total
	
roman='mmmdccclxxxviii'
print(numerus(roman))
