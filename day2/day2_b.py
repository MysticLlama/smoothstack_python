def one(): #create a list of varried values
	li = [23,"Taco",5.33343]
	print(li)
	

def two():#index a multi-dimensional list
	li = [1,1,[1,2]]
	print(li[2][1])
	
	
def three(): #get elemnst 2 onwards
	lst = ["a","b","c"]
	print(lst[1:]) #should be ["b","c"]
	
def four(): #create a dict of weekdays
	week = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
	print (week)
	
	
def five(): #create a dictionary with a list as a value
	D={"k1":[1,2,3]}
	print(D["k1"][1])


def six(): #convert a multi-dimensional list to a touple
	li = [1,[2,3]]
	print(tuple(li))
	
def seven(): #convert a string to a set
	print(set("Mississippi"))
	
def eight(): #add an x to the string
	mi= set("Mississippi")
	mi = list(mi)
	mi.append("X")
	mi = set(mi)
	print (mi)
	
def nine(): #print a list as a set
	print(set([1,1,2,3]))
	

def question1(): #print numbers from 2000,3200 that is divisble by 7, but not 5
	nums =[]
	
	for i in range(1999,3200):
		if i%7==0 and i%5 != 0:
			nums.append(i)
			
	print(nums)
	
def question2(): #prompt user to factorial a number
	print(fact(int(input("Enter a number to Factorial: "))))




def fact(x): #naive recurisve factorial
	if x==0:
		return 1
	return x*fact(x-1)
	
	
	
	
	
def question3(): #create a dictionary of numbers claing up based on input
	d ={}
	x = int(input("Enter a number of dict entries to make: "))
	
	if(x<1):
		print({})
	
	for i in range(0,x+1):
		d[i]=i*i
		
	print (d)
	
	
	
def question4(): #get comma seperated numbers to reprint as list and tuple
	v = input("Enter comma-seperated numbers to convert to list and tuple: ")
	l = v.split(",")
	t = tuple(l)
	print(l)
	print(t)
	
	
	
	
	
	
class InputOutString(object):
	def __init__(self):
		self.s=""
		
		
	def getString(self):
		self.s = input("Enter a string: ")
		
		
	def printString(self):
		print(self.s.upper())
		
	
	

def main():
	one()
	two()
	three()
	four()
	five()
	six()
	seven()
	eight()
	nine()
	
	question1()
	question2()
	question3()
	question4()
	
	ob = InputOutString()
	ob.getString()
	ob.printString()
	
	
main()