def bmi(l,*args):
	wk=""
	w=0
	h=0
	sol=""
	ind=0
	for line in args:
		wk= line.split(" ")
		w=float(wk[0])
		h = float(wk[1])
		
		ind = (w)/(h)**2
		
		if ind <18.5:
			sol+="under "
		elif ind >= 18.5 and ind<25:
			sol+="normal "
		elif ind >= 25 and ind <30:
			sol+="over "
		else:
			sol+= "obese "
	return sol
	
	
	
def main():
	print(bmi(3,"80 1.73","55 1.58","49 1.91"))
	
	
main()