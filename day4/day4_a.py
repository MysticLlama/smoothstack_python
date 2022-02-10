def func():
	print("Hello World")
	
def func1(name):
	print("Hi My name is Google")
	
def func3(x,y,z):
	if z:
		return x
	else:
		return y
		
def func4(x,y):
	return x*y
	
def is_even(x):
	return (x%2==0)
	
def gt(x,y):
	return x>y
	
	
def sum_args(*args):
	sum=0
	for num in args:
		sum+=num
		
	return sum
	
def evens(*args):
	evens =[]
	for num in args:
		if num%2==0:
			evens.append(num)
	return evens
	
def evencase(s):
	evens = s[0::2]
	odds = s[1::2]
	sol=""
	l=0
	if len(evens)>len(odds):
		l = len(evens)
	else:
		l=len(odds)
	for i in range(l):
		if i<len(evens):
			sol+=evens[i]
		if i<len(odds):
			sol+=odds[i].upper()
	return sol
	
def compare(x,y):
	if x%2==0 and y%2==0:
		if x>y:
			return y
		else:
			return x
			
	else:
		if x>y:
			return x
		else:
			return y
def samestart(x,y):
	return x[0].lower() == y[0].lower()
	

def first_and_forth(s):
	sol=""
	for i in range(len(s)):
		if i==0 or i==3:
			sol+= s[i].upper()
		else:
			sol+= s[i]
	return sol
	
	
	
	
def main():
	func()
	func1("Marmalade")
	print(func3(1,2,True))
	print(func4(4,5))
	print(is_even(5))
	print(is_even(4))
	print(gt(4,5))
	print(gt(5,4))
	print(sum_args(1,2,3,4,5))
	print(evens(1,2,3,4,5,6,7,8,9,10))
	print(evencase("spaghetti"))
	print(compare(5,6))
	print(samestart("taco","transformer"))
	print(first_and_forth("butterfly"))
	
	
	
main()
	
	