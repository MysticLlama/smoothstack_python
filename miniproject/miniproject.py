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
		
		sheet = wb.active
		
		for i in range(1,15):
			for j in range(1,6):
				cell = sheet.cell(row=i,column=j)
				print(cell.value)
		
		
		#cell = sheet.cell(row=2,column = 3)
		#print(cell.value)
			
			
	except FileNotFoundError as e:
		print("Invalid File")
		
		logging.error("Tried to open invalid file with name: "+filename)
	
	
	
	
main()


