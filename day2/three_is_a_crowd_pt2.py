def crowd_test(li):
	
	if len(li) >3:
		print("The room is crowded")
	else:
		print("The room isn't crowded")





def main():
	people=["Jerry","Garry","John","Rebecca"]
	crowd_test(people)
	
	people= people[:2]
	crowd_test(people)
	
main()