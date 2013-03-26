
word = raw_input("write word: ")
def check(word):	
	i = len(word)-1
	c=0
	for count in range(0,i+1):
		compare = i - count

		if word[count] == word[compare]:
			c=c+1
			

	if(i+1==c):
		return"same"		
	else:
		return"different"
 
print check (word)