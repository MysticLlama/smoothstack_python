def one():
	print("1)\n")
	print(50+50)
	print(100-10)
	print()
	
def two():
	print("2)\n")
	print("uh")
	print(6^6)
	print(6**6)
	print(6+6+6+6+6+6)
	print()
	
	
def three():
	print("3)\n")
	print("Hello World")
	print("Hello World : 10")
	print()
	
	
# def four(p,r,l):
	# #given a principal p that increases at rate r p/a, what do i need to pay in order to pay it off within l months?
	# sum = p
	# m =0
	# for i in range(0,l):
		# sum *= 1+((r/12)/100)
	# #print(sum)	
	# print(round(sum/l))
	
	
def four_kek(p,r,l):
	yrs =l//12
	extra = l%12
	sum =p
	for i in range(0,yrs):
		sum *= 1+(r/100)
		
	
	c = sum * (r/100)
	sum += (c/(12-extra))
	print(round(sum/l))
	
	
def test(p,r,a,l):
	sum =p
	count =0
	while(sum >0):
		sum *= 1+((r/12)/100)
		sum -=a
		count +=1
		
		if(count > l):
			return(l+1,p)
	
	return (count,sum)
	
	
def four_kms(p,r,l):
	m = 10000
	t =test(p,r,m,l)
	smol = m
	sol = 0
	while( t  !=(l,0)):
		#print("tried ",m, t)
		m -=1
		if(abs(t[1]) < smol):
			smol =abs(t[1])
			sol = m+1	
		
		if(m<1):
			#print("coulden't find a valid M")
			break
		t = test(p,r,m,l)
	print(sol)
		
	
def four(p,r,l):
	four_kms(p,r,l)
	
	
def main():

	one()
	two()
	three()
	#four(800000,6,103)
	#four_kek(800000,6,103)
	#print(test(800000,6,10000))
	#print(test(800000,6,9960))
	#print(test(800000,6,9957))
	#print(test(800000,6,3999))
	print("4)")
	four(800000,6,103)




main()