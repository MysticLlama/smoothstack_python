def one():
	print("Example 1)\n")
	print(50+50)
	print(100-10)
	print((50+50)+(100-10))
	print()
	
def two():
	print("Example 2)\n")
	print(6^6)
	#print(30+*6) # this is not valid syntax
	print(6**6)
	print(6+6+6+6+6+6)
	print()
	
	
def three():
	print("Example 3)\n")
	print("Hello World")
	print("Hello World : 10")
	print()
	

	

	
#used to help check if payment amount "a" satisfies the mortgage given "p" principal, "r" anual rate, "l" length of payment.
#returns touple of (number payments of "a" required to pay off mortgage, remaining payment)  
def test(p,r,a,l):
	sum =p #keeps track of working sum of payment left
	count =0 #tracks number of paymenst required
	while(sum >0):
		sum *= 1+((r/12)/100) ##apply interest for the month
		sum -=a #subtract the amount we're trying
		count +=1 #++ to mark down this month
		
		if(count > l): #if the number of payments needed exceeds the length we're given, we can stop early with a bad value that auto-fails
			return(l+1,p*l) #return a pair of numbers that could not possibly work to mark this try as irrelevant
	
	return (count,sum) #return as touple for debugging
	


#find a constant monthly payment that best pays off the mortgage with "p" principal, "r" anual rate increase, "l" length of payment
#such that the monthly payment is under 10,000 per month.	
def four(p,r,l): 
	m = 10000 #spec defines 10,000 as the maximum possible monthly payment.
	t =test(p,r,m,l) #used to track current iteration of test
	smol = m #value used to track smallest value
	sol = 0 #solution value, define as 0, for invalid payments should we not find a valid value for monthly payment
	while( True):
		m -=1 #check every amount from 10,000 down to 0 until we find a good value
		if(abs(t[1]) < smol): #keep track of the smallest end-of-period difference to find best value
			smol =abs(t[1]) #track absolute value
			sol = m+1 #add 1 to m because of indexing order.	
		
		if(m<1):
			break #stop looking if m would be an invalid payment.
		t = test(p,r,m,l) #set next m to pay
	print(sol) #"return" our value via print
		
	
	
def main():

	one()
	two()
	three()
	print("Example 4)")
	four(800000,6,103)


main()