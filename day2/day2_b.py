def one():
	li = [23,"Taco",5.33343]
	print(li)
	

def two():
	li = [1,1,[1,2]]
	print(li[2][1])
	
	
def three():
	lst = ["a","b","c"]
	print(lst[1:]) #should be ["b","c"]
	
def four():
	week = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
	print (week)
	
	
def five():
	D={"k1":[1,2,3]}
	print(D["k1"][1])


def six():
	li = [1,[2,3]]
	print(tuple(li))
	
def seven():
	print(set("Mississippi"))
	
def eight():
	mi= set("Mississippi")
	mi = list(mi)
	mi.append("X")
	mi = set(mi)
	print (mi)
	
def nine():
	print(set([1,1,2,3]))
	

def question1():
	nums =[]
	
	for i in range(1999,3200):
		if i%7==0 and i%5 != 0:
			nums.append(i)
			
	print(nums)
	
def question2():
	print(fact(int(input("Enter a number to Factorial: "))))




def fact(x):
	if x==0:
		return 1
	return x*fact(x-1)
	
	
	
	
	
def question3():
	d ={}
	x = int(input("Enter a number of dict entries to make: "))
	
	if(x<1):
		print({})
	
	for i in range(0,x+1):
		d[i]=i*i
		
	print (d)
	
	
	
def question4():
	v = input("Enter comma-seperated numbers to conert to list and tuple: ")
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