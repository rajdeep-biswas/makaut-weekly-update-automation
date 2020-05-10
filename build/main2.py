# pip install selenium
# find and install browser version specific webdrivers
# date_tme format "2020-05-16 22:55", "1997-10-28 00:35"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd

driver = webdriver.Chrome(executable_path='C:\\Users\\Rajdeep\\Desktop\\chromedriver.exe')

teachers = {
    "Sujata Ghatak": "Sujata  Ghatak( Bachelo of Computer Application )",
    "Manjima Saha": "Manjima  Saha( Bachelor of Computer Application )",
    "Amitava Chatterjee": "Amitava Chattopadhyay( Bachelor of Computer Application )",
    "Ankan Bhowmik": "Ankan Bhowmik( Bachelor of Computer Application )"
}

xlid = 2

xlname = "sheets/" + str(xlid) + ".xlsx"
df = pd.read_excel(xlname)

driver.get("https://makaut1.ucanapply.com/")
driver.find_element(By.XPATH, '//div[@class="databox-left bg-themeprimary"]').click()
sleep(1)
driver.find_element(By.XPATH, '//input[@id="username"]').send_keys("10401217055")
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("OVBH7")
driver.find_element(By.XPATH, '//a[@class="btn btn-success btn-lg"]').click()

for index, row in df.iterrows():
    
    sleep(3)
    driver.get("https://makaut1.ucanapply.com/smartexam/public/student/week-report-activity/create")

    driver.find_element(By.XPATH, '//select[@id="week"]').click()
    sleep(1)
    weekval = "10" + str(xlid)
    driver.find_element(By.XPATH, '//option[@value=' + weekval + ']').click()

    select = Select(driver.find_element_by_id('SEMCODE'))
    sleep(1)
    select.select_by_index(1)
    
    select = Select(driver.find_element_by_id('COURSECD'))
    sleep(1)
    select.select_by_index(1)
    
    select = Select(driver.find_element_by_id('SUBJECTCODE'))
    sleep(1)
    if row["Subject"] == "Networking":
        select.select_by_index(4)
    else:
        select.select_by_index(5)

    driver.find_element(By.XPATH, '//textarea[@id="topic_covered"]').send_keys(row["Topic Covered"])
    driver.find_element(By.XPATH, '//textarea[@id="platform_used"]').send_keys(row["Platform Used"])

    select = Select(driver.find_element_by_id('class_taken_by'))
    sleep(1)
    select.select_by_visible_text(teachers[row["Class Taken By"]])
    
    driver.execute_script('document.getElementById("date_tme").removeAttribute("readonly")')
    driver.execute_script('var aa=document.getElementsByClassName("datetimepicker datetimepicker-dropdown-bottom-right dropdown-menu")[0];aa.parentNode.removeChild(aa)')
    driver.find_element(By.XPATH, '//input[@id="date_tme"]').send_keys(row["Date/Time"])

    # have format: "24.04.2020,10AM" expected: "2020-05-16 22:55"

    driver.find_element(By.XPATH, '//input[@id="record_lecture_upload_link"]').send_keys(row["Record Lecture Upload Link"])
    driver.find_element(By.XPATH, '//input[@id="duration_in_min"]').send_keys(row["Duration in Min"])
    driver.find_element(By.XPATH, '//input[@id="post_class_interraction_note"]').send_keys(row["Post Class Interraction Note"])
    driver.find_element(By.XPATH, '//textarea[@id="assignment_received"]').send_keys(row["Assignment Received"])
    driver.find_element(By.XPATH, '//input[@id="assignment_submitted"]').send_keys(row["Assignment Submitted"])
    driver.find_element(By.XPATH, '//input[@id="test_attended_if_any"]').send_keys(row["Test Attended if any"])
    driver.find_element(By.XPATH, '//textarea[@id="daily_self_acitvity"]').send_keys(row["Daily Self Activity"])
    driver.find_element(By.XPATH, '//textarea[@id="remark"]').send_keys("NA")

    driver.find_element(By.XPATH, '//input[@id="btnSubmit"]').click()

    break
