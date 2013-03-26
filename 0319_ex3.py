def get_input():
	num=input ("input your number:")

	if num > 0 and num < 10:
		give= num+10
		print give

	elif num > 10 and num <100:
		give = num*0.1
		print give

	else:
		print "false"

get_input()