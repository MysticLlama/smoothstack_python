from random import random


def one():
	arr=[]
	for i in range(1499,2700):
		if i%7 ==0 and i%5!=0:
			arr.append(i)
			
	print(arr)
	
	
def two(t,s):
	if s.lower()=="c" or s.lower() =="celsius":
		temp = (t-32) * (5/9)
		print(round(temp))
	else:
		temp =(t*(9/5)) +32
		print(round(temp))
		
	
def three():
	number = round(random())*9
	if number ==0:
		number =1
	
	guess = int(input("Guess a number between 1 and 9! "))
	
	while(guess != number):
		guess = int(input("Wrong guess! "))
	print("Well guessed!")

def four():
	for i in range(0,10):
		stars=""
		#q=0
		if i > 5:
			q=(10-i)
		else:
			q= i
		for j in range(0,q):
			stars +="*"
		print (stars)
		
		
def six():
	word = input("Enter a word to reverse: ")
	print(word[::-1])
	
	
def seven(li):
	odds=0
	evens=0
	for num in li:
		if num%2==0:
			evens +=1
		else:
			odds +=1
	print("Number of even numbers : ",evens)
	print("Number of odd numbers : ",odds)
	
	
def eight():
	datalist =[1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class":'V',"section":'A'}]

	for item in datalist:
		print(type(item))
		
def nine():
	sol =""
	for i in range(0,7):
		if i == 3 or i == 6:
			continue
		sol += str(i)+" "
		
	print(sol)
	
	
	
def main():
	one()
	two(60,"f")
	two(45,"c")
	three()
	four()
	#five()
	six()
	seven((1,2,3,4,5,6,7,8,9))
	eight()
	nine()
	
main()