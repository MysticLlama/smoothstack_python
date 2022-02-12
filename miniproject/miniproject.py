import csv
import pandas as pd
import logging
import openpyxl
from datetime import date



def main():
	logging.basicConfig(filename="log.log",level=logging.DEBUG)
	

	
	name = input("Enter name of file: ")
	
	
	
	#print(filename)
	try:
		wb= openpyxl.load_workbook(filename=name)
			#print (file)
		logging.info(str(date.today())+": Started Program")
		
		name = name.replace(".xlsx","")
		items = name.split("_")
		#print(items)
		month =items[-2]
		year= items[-1]
		
		months = {"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
		#print((month,year))
		
		
		sheet = wb.active
		sol=[]
		found=False
		for i in range(1,100):
			for j in range(1,100):
				cell = sheet.cell(row=i,column=j)
				logging.info(str(date.today())+": Looking at cell "+str(i)+","+str(j))
				#print(str(cell.value).split("-"))
				wk=str(cell.value).split("-")
				if(len(wk ) >1):
					entry =(wk[0],int(wk[1]))
					if(year ==entry[0] and months[month]== entry[1]):
						for k in range(1,6):
							sol.append(sheet.cell(row=i,column=j+k).value)
						found = True
						logging.info(str(date.today())+": Found entry at "+str(i)+","+str(j))
						
						break
			if found:
				break
		#print(sol)
		
		print("Calls Offered: ",sol[0])
		print("Abandon after 30s : ",sol[1]*100,"%")
		print("FCR : ",sol[2]*100,"%")
		print("DSAT : ",sol[3]*100,"%")
		print("CSAT : ",sol[4]*100,"%")
		
					#print((wk[0],int(wk[1])))
		
		
		#cell = sheet.cell(row=2,column = 3)
		#print(cell.value)
			
			
	except FileNotFoundError as e:
		print("Could not find that file")
		
		logging.error(str(date.today())+": Tried to open nonexistant file with name: "+name)
	except openpyxl.utils.exceptions.InvalidFileException as e:
		print("Invalid File")
		
		logging.error(str(date.today())+": Tried to open invalid file with name: "+name)
	
	
	
	
main()


