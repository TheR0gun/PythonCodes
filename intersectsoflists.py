hello=['a','g','t','d','e','u','x']
hi=['z','f','g','e','r','f','h']
def intersect(alist,blist):
	commonlist=[]
	for l in alist:
		for j in blist:
			if l == j:
				commonlist.append(l)

	return commonlist
clist= intersect(hello,hi)
print(clist)

		
print(list(set(hello).intersection(hi)))

def pair(alist,blist):
	for a in alist:
		for b in blist:
			print(a + ',' + b)
	return
pair(hello,hi)