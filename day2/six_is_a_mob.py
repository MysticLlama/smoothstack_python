def crowd_test(li):
	
	if len(li) >5:
		print("There is a mob")
	elif len(li) > 3:
		print("The room is crowded")
	elif len(li)>0:
		print("The room isn't crowded")
	else:
		print("The room is empty")




def main():
	people=["Jerry","Garry","John","Rebecca"] #len of 4
	crowd_test(people)
	
	people= people[:2] #len of 2
	crowd_test(people)
	
	people+= ["Barry","Carl","Thomas","Joe","Sally"] #len of 6
	crowd_test(people)
	
	people= [] #empty list (len of 0)
	crowd_test(people)
	
main()