from random import random


def one(): #print numbers from 1500,2700 that are divisiible by 7, but not 5
	arr=[]
	for i in range(1500,2700):
		if i%7 ==0 and i%5!=0:
			arr.append(i)
			
	print(arr)
	
	
def two(t,s): #convert between celsius and fahrenheit 
	if s.lower()=="c" or s.lower() =="celsius":
		temp = (t-32) * (5/9)
		print(round(temp))
	else:
		temp =(t*(9/5)) +32
		print(round(temp))
		
	
def three(): #prompt the user for a guess between 1-9
	number = round(random())*9
	if number ==0:
		number =1
	
	guess = int(input("Guess a number between 1 and 9! "))
	
	while(guess != number):
		guess = int(input("Wrong guess! "))
	print("Well guessed!")

def four(): #print a sideways pyramid patter of *s
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
		
		
def six(): #prompt user to reverse a word
	word = input("Enter a word to reverse: ")
	print(word[::-1])
	
	
def seven(li): #count number of evens and odds in an input list
	odds=0
	evens=0
	for num in li:
		if num%2==0:
			evens +=1
		else:
			odds +=1
	print("Number of even numbers : ",evens)
	print("Number of odd numbers : ",odds)
	
	
def eight(): #print the types of the items in the list
	datalist =[1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class":'V',"section":'A'}]

	for item in datalist:
		print(type(item))
		
def nine():#print numbers between 1-7 that aren't 3 or 6
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