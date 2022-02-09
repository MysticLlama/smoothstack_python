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
	print(set(s))
	
def five(s): #return whether s is a palindrome, with string Y or N for yes,no respectievly.
	if type(s) is not str:
		print("N")
		return
	
	if len(s) <2:
		print("N")
		return
	s= s.lower()	
	punc = " !?.,;:@#$%^&*<>()-_+=[]{}\\\'\""
	
	for c in s:
		if c in punc:
			s = s.replace(c,"")
			
	if s[::-1] == s:
		print("Y")
	else:
		print("N")
		
		
		
		
def main():
	one()
	two()
	three()
	four()
	
	five("Some men interpret nine memos")
	
main()
