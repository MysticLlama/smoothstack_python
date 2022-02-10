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
	
	guess = int(input("Guess a number between 1 and 9! "))
	
	while(guess != number):
		guess = int(input("Wrong guess! "))
	print("Well guessed!")
