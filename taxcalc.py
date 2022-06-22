# tax calculator.

def taxcalc():
	hours = input('Employee hours: ')
	rate = input('Pay rate per hour: ')
	total = float(rate) * float(hours)
	print(total,"Dollars")
taxcalc()
