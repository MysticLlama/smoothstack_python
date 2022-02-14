import csv
import pandas as pd
import logging
import openpyxl
from datetime import date



def main():
	logging.basicConfig(filename="log.log",level=logging.DEBUG)
	

	
	name = input("Enter name of file: ")
	
	
	
	try:
		wb= openpyxl.load_workbook(filename=name)
		logging.info(str(date.today())+": Started Program")
		
		name = name.replace(".xlsx","")
		items = name.split("_")
		month =items[-2]
		year= items[-1]
		
		months = {"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
		
		
		sheet = wb.active
		sol=[]
		headers ={"Calls Offered":0,"Abandon after 30s":0,"FCR":0,"DSAT":0,"CSAT":0}
		found=False
		for i in range(1,100):
			for j in range(1,100):
				cell = sheet.cell(row=i,column=j)
				logging.info(str(date.today())+": Looking at cell "+str(i)+","+str(j))
				wk=str(cell.value).split("-")
				if(len(wk ) >1):
					entry =(wk[0],int(wk[1]))
					if(year ==entry[0] and months[month]== entry[1]):
						for k in range(1,6):
							sol.append(sheet.cell(row=i,column=j+k).value)
						found = True
						logging.info(str(date.today())+": Found entry at "+str(i)+","+str(j))
						
						break
				elif(len(wk) ==1):
					if(wk[0].strip() in headers):
						headers[wk[0].strip()]=j
						logging.info(str(date.today())+": Found Header at "+str(i)+","+str(j))
			if found:
				logging.info(str(date.today())+": Found All required entries")
				break
		if not found:
			logging.error(str(date.today())+": Exausted search within tolerance value")
			print("Data not found")
			return
		
		headers = dict(sorted(headers.items(), key=lambda item: item[1])) ##sort the headers list
		head_l = list(headers.keys()) #makes headers indexable in order they were retireved in
		logging.info(str(date.today())+": Sorted Headers list for display")
		print(head_l[0],": ",sol[0])
		logging.info(str(date.today())+": Displayed item 1")
		print(head_l[1],": ",sol[1]*100,"%")
		logging.info(str(date.today())+": Displayed item 2")
		print(head_l[2],": ",sol[2]*100,"%")
		logging.info(str(date.today())+": Displayed item 3")
		print(head_l[3],": ",sol[3]*100,"%")
		logging.info(str(date.today())+": Displayed item 4")
		print(head_l[4],": ",sol[4]*100,"%")
		logging.info(str(date.today())+": Displayed item 5")
		
		logging.info(str(date.today())+": Program Finished")
			
			
	except FileNotFoundError as e:
		print("Could not find that file")
		
		logging.error(str(date.today())+": Tried to open nonexistant file with name: "+name)
	except openpyxl.utils.exceptions.InvalidFileException as e:
		print("Invalid File")
		
		logging.error(str(date.today())+": Tried to open invalid file with name: "+name)
	
	
	
	
main()


