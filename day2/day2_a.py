def one():
	s = "Hello World"
	print (s[8]) #should be "r"
	
def two():
	s = "thinker"
	print( s[2:5]) # should be "ink"
	
	s= "hello"
	print(s[1]) #should be "e"
	
	
	
def three():	
	s= "Sammy"
	print(s[2:]) # should be "mmy"
	

def four():
	s = "Mississippi"
	print(set(s)) #should be {"M,"i","s","p"} in any order
	
def test(s): #return whether s is a palindrome, with string Y or N for yes,no respectievly.
	if type(s) is not str: #not a palidrome if its not a string
		return "N"
	
	if len(s) <2: #1 or 0 character strings aren't palindromes
		return "N"
		
	s= s.lower() #convert string to lowercase	
	punc = " !?.,;:@#$%^&*<>()-_+=[]{}\\\'\""
	
	for c in s:
		if c in punc:
			s = s.replace(c,"") #remove any punctuation
			
	if s[::-1] == s: #if this converted string is the same forwrads and backwards, its a palindrome
		return "Y"
	else:
		return "N" #no otherwise
		
def five(length,*words): # take length, and inputted words to check if they are palindromes
	sol=""
	
	for i in range(0,length):
		sol +=test(words[i])
		sol += " "
		
	print(sol)
	
		
		
		
		
		
		
		
def main():
	one()
	two()
	three()
	four()
	
	five(3,"Stars","O, a kak Uwakov lil vo kawu kakao!","Some men interpret nine memos")
	
main()
