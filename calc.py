# Mark: The basic operations of our calculator
def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mul(a, b):
	return a * b #TODO: Your code here

def div(a, b):
	return a / b

def mod(a, b):
	return a % b

#Mark: Our main method which will run when we call the application
def main():
	a = 66	#First number
	b = 33	#Second number
	result = mul(a,b)	# First divided by second
	print("The result is %.2f" % result)

if __name__ == "__main__":
	main()
