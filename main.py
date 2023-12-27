import time
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
#open the browser
driver = webdriver.Chrome()
#open the given web URL
driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")
driver.maximize_window()
#find and click table data element
driver.find_element(By.XPATH,"/html/body/div/div[3]/details/summary").click()
#clearing existing data from the input text box
driver.find_element(By.XPATH,"//*[@id='jsondata']").clear()
#passing data to the input text box
driver.find_element(By.XPATH,"//*[@id='jsondata']").send_keys('[{"name":"Bob","age":20,"gender":"male"},{"name":"George","age":42,"gender":"male"},{"name":"Sara","age":42,"gender":"female"},{"name":"Conor","age":40,"gender":"male"},{"name":"Jennifer","age":42,"gender":"female"}]')
#click refresh table button
driver.find_element(By.XPATH,"//*[@id='refreshtable']").click()
#finding table on the web and storing it to table variable
table=driver.find_element(By.XPATH,"//*[@id='dynamictable']")
#finding rows in table
rows=table.find_elements(By.TAG_NAME,"tr")
#printing table values
for row in rows[1:]:
    print([cell.text for cell in row.find_elements(By.TAG_NAME,"td")])
time.sleep(10.0)