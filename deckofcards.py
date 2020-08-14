numbers=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
symbols=['spades','hearts','diamonds','clubs']
for s in symbols:
	for n in numbers:
		print(n + ' of ' + s.title() )

count=0
number=1
while number <= 1000000000000:
	number *= 2
	print(number)
	count += 1
print(count)