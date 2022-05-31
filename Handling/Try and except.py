# Working of try()
def divide(x, y):
	try:
		result = x // y
		print("Yeah ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

# Parameters
divide(3, 0)
