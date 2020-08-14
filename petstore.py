pets={'bird':3.50,'cat':5.00,'dog':7.25,'gerbil':1.50}

inp = input("Enter a pet:")

def pet_store(inp):
	found=False
	for key,value in pets.items():
		if inp==key:
			print(inp + ' is $' + str(value))
			found = True
			return(found)

while not pet_store(inp):
	inp= input('I didnt find that in our stock. Can you select another pet:')
	
	
 		
	
	




	