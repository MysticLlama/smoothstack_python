def one():
	print("Example 1)\n")
	print(50+50)
	print(100-10)
	print((50+50)+(100-10))
	print()
	
def two():
	print("Example 2)\n")
	print(6^6)
	print(6**6)
	print(6+6+6+6+6+6)
	print()
	
	
def three():
	print("Example 3)\n")
	print("Hello World")
	print("Hello World : 10")
	print()
	

	

	
	
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
	
	
def four(p,r,l):
	m = 10000
	t =test(p,r,m,l)
	smol = m
	sol = 0
	while( t  !=(l,0)):
		m -=1
		if(abs(t[1]) < smol):
			smol =abs(t[1])
			sol = m+1	
		
		if(m<1):
			break
		t = test(p,r,m,l)
	print(sol)
		
	
	
def main():

	one()
	two()
	three()
	print("Example 4)")
	four(800000,6,103)


main()