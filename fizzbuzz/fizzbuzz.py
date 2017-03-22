# def fizzbuzz(number):
# 
# 	fizz_eq = float(number)/3.0
# 	fizz_eq = str(fizz_eq)
# 	
# 	if fizz_eq.split('.')[1] == '0':
# 		return 'fizz'
# 
# 	elif type(number) == int:
# 		return number
		
def fizzbuzz(number):

# 	assert (type(number) == int), "Number is not an int"
	
	try:
		if type(number) != int:
			raise TypeError("That is not an int!")
	
	elif number % 3 == 0 and number % 5 == 0:
		return 'fizzbuzz'
	
	elif number % 3 == 0:
		return 'fizz'
		
	elif number % 5 == 0:
		return 'buzz'
		
	else:
		return number