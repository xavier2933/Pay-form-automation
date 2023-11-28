#################################################################
# formAutomation.py
# Author: Xavier O'Keefe
# 
# This uses Selenium to automate my weekly time sheet for my lab.
#################################################################
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv
import secretFile

class readData:
    # Set initial params for data that is not easily read from csv file
    def __init__(self, inFile):
        self.days = ["Sun", "Mon", "Tues", "Weds", "Thurs", "Fri", "Sat"]
        self.browser = webdriver.Chrome()
        self.totalHoursWorkedWeek1 = 0
        self.totalHoursWorkedWeek2 = 0
        self.bigTotalWorked = 0
##################################################################################################
#                        STUFF YOU NEED TO CHANGE
# - I used a secret file, replace that whole variable with your info in string form
# - Find your info in the .html doc, make sure the variable is the exact same
##################################################################################################
        self.docToRead = inFile
        self.name = "Xavier O'Keefe"
        self.email = "xaok7569@colorado.edu"
        self.sup_Name = secretFile.superName
        self.sup_Email = secretFile.superEmail
        self.url = secretFile.link

    # Load the browser
    def getBrowser(self):
        self.browser.get(self.url)
        wait = WebDriverWait(self.browser, 100) # 100 secs to wait
        try:
            # Wait until user logs in
            wait.until(EC.element_to_be_clickable((By.NAME, 'realname')))
            self.addData() 
        finally: 
            # Quit if no login/invalid login
            self.browser.quit()
            print("Timed out! Try again")
            exit()

    # Function to read the CSV file and add data into the form
    def addData(self):
        name = Select(self.browser.find_element(By.NAME, "realname"))
        name.select_by_visible_text(self.name)
        email = self.browser.find_element(By.NAME, "email")
        email.send_keys(self.email)
        supName = Select(self.browser.find_element(By.NAME, "Supervisor"))
        supName.select_by_visible_text(self.sup_Name)
        supEmail = Select(self.browser.find_element(By.NAME, "recipient"))
        supEmail.select_by_visible_text(self.sup_Email)

        # Weird iteration because of form structure
        i = 0
        j = 0
        with open(self.docToRead) as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            for row in csvReader:
                if(i < 7): # Hardcode for first week
                    (date, inner, out, total) = row
                    date1 = self.browser.find_element(By.NAME, "Date_" + self.days[i] + "_Week1")
                    date1.send_keys(str(date))
                    in1 = self.browser.find_element(By.NAME, "In_" + self.days[i] + "_Week1")
                    in1.send_keys(str(inner))
                    out1 = self.browser.find_element(By.NAME, "Out_" + self.days[i] + "_Week1")
                    out1.send_keys(str(out))
                    total1 = self.browser.find_element(By.NAME, "Total_Hours_" + self.days[i] + "_Week1")
                    self.totalHoursWorkedWeek1 += float(total) # store data for total hours
                    total1.send_keys(str(total))
                    i += 1
                else:
                    (date, inner, out, total) = row
                    date2 = self.browser.find_element(By.NAME, "Date_" + self.days[j] + "_Week2")
                    date2.send_keys(str(date))
                    in2 = self.browser.find_element(By.NAME, "In_" + self.days[j] + "_Week2")
                    in2.send_keys(str(inner))
                    out2 = self.browser.find_element(By.NAME, "Out_" + self.days[j] + "_Week2")
                    out2.send_keys(str(out))
                    total2 = self.browser.find_element(By.NAME, "Total_Hours_" + self.days[j] + "_Week2")
                    self.totalHoursWorkedWeek2 += float(total)
                    total2.send_keys(str(total))
                    if j == 6: # last day of pay period
                        endDateVal = date
                    j +=1     

        hours1 = self.browser.find_element(By.NAME, "Total_Hours_Week1")
        hours1.send_keys(str(self.totalHoursWorkedWeek1))
        hours2 = self.browser.find_element(By.NAME, "Total_Hours_Week2")
        hours2.send_keys(str(self.totalHoursWorkedWeek2)) 
        bigTotal = self.browser.find_element(By.NAME, "Total_Hours_for_Pay_Period")
        self.bigTotalWorked = self.totalHoursWorkedWeek1 + self.totalHoursWorkedWeek2
        bigTotal.send_keys(str(self.bigTotalWorked))  
        endDate = self.browser.find_element(By.NAME, "Pay_Period_End_Date")
        endDate.send_keys(str(endDateVal))
        time.sleep(100)

    # Quits the browser
    def quitBrowser(self):
        self.browser.quit()

if __name__ == "__main__":
    print()
    file = input("Which file??  >> ")
    read = readData(file)
    read.getBrowser()
    read.quitBrowser()

