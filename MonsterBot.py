from selenium import webdriver
from time import sleep
import xlsxwriter


web = webdriver.Chrome()


#Define function for opening the website
def openweb():
	
	web.maximize_window()
	web.get('https://www.monsterboard.nl')
	sleep(2)

#Function loop for writing the iteration inside the other iteration
def lookjob(k_list, r_list, row):   #k_list, r_list are the arguments given by the function as list of words to search.
	
	for j in range(len(r_list)):   #This loop is looking the keywords along the different locations in the r_list (region list)
			
		if j==0 and i==0: 			# Here j and i has to be 0 because the first iteration is done in the main page of the web, then the textboxes has different xpath      
			column=j+1
			web.find_element_by_id('q1').send_keys(k_list[i])
			web.find_element_by_id('where1').send_keys(r_list[j])
			web.find_element_by_id('doQuickSearch').click()
			sleep(2)
			data = web.find_element_by_xpath('/html/body/div[2]/section/div/header/h2').text 	#This storage the text in the web in the 'data' variable.	 
			sleep(1)
			page.write(row, column, data)			#This write the first number result in the excel file
			page.write(0, j+1, r_list[j])
			print(data)								#This print is just a safe check of correct working
			sleep(1)

			
			
		else:						#Here are selecting the textboxes after a first search. 
			column=j+1
			web.find_element_by_id('keywords2').click()
			sleep(2)
			web.find_element_by_class_name('input-clear').click()
			sleep(1)
			web.find_element_by_id('keywords2').send_keys(k_list[i])
			web.find_element_by_id('location').click()
			sleep(2)
			web.find_element_by_xpath('//*[@id="quickJobSearch"]/div[2]/div/span[3]').click()
			sleep(1)
			web.find_element_by_id('location').send_keys(r_list[j])
			web.find_element_by_id('doQuickSearch').click()
			sleep(2)
			data = web.find_element_by_css_selector('body > div.page-layout > section > div > header > h2').text 	#This storage the text in the web in the 'data' variable.	
			sleep(1)
			page.write(row, column, data)			#This write the number result in the excel file
			page.write(0, j+1, r_list[j])
			print(data)								#This print is just a safe check of correct working

		j=j+1	
		
#def rowandcolumn(k_list,r_list):
#	for i in range(len(kr_list):
#		row=1
#		column
#		page.write(row, column, k_list[i])	


k_list = ['CSS', 'python', 'javascript']			#This list has to be replazed by a entered one by the user
r_list = ['amsterdam', 'eindhoven', 'utrecht']		#This list has to be replazed by a entered one by the user
i=0
j=0



openweb()

book = xlsxwriter.Workbook('JobAnalysis.xlsx')		#Creates the xlsx
page = book.add_worksheet('Monsterboard')			#Creates the worksheet in the woorbook created



row=1
for i in range(len(k_list)):		#This loop is going along the keyword list. For each keyword in the list, enter in the function lookjob where each region is checked.
	
	lookjob(k_list, r_list, row)
	page.write(i+1, 0, k_list[i])
	i=i+1
	row=row+1
	sleep(1)


book.close()
sleep(2)
