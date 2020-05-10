# pip install selenium
# find and install browser version specific webdrivers
# date_tme format "2020-05-16 22:55"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd

driver = webdriver.Chrome(executable_path='C:\\Users\\Rajdeep\\Desktop\\chromedriver.exe')
ac = ActionChains(driver)

df = pd.read_excel("sheets/2.xlsx")

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
    driver.find_element(By.XPATH, '//option[@value="102"]').click()

    driver.find_element(By.XPATH, '//select[@id="SEMCODE"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//option[@value="SM06"]').click()
    
    driver.find_element(By.XPATH, '//select[@id="COURSECD"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//option[@value="C000004"]').click()
    
    driver.find_element(By.XPATH, '//select[@id="SUBJECTCODE"]').click()
    sleep(3)
    if row["Subject"] == "Networking":
        driver.find_element(By.XPATH, '//option[@value="SU00008635"]').click()
    else:
        driver.find_element(By.XPATH, '//option[@value="SU00008639"]').click()

    driver.find_element(By.XPATH, '//textarea[@id="topic_covered"]').send_keys(row["Topic Covered"])
    driver.find_element(By.XPATH, '//textarea[@id="platform_used"]').send_keys(row["Platform Used"])
    
    driver.find_element(By.XPATH, '//select[@id="class_taken_by"]').click()
    sleep(3)
    if row["Class Taken By"] == "Ankan Bhowmik":
        driver.find_element(By.XPATH, '//option[@value="180529"]').click()
    elif row["Class Taken By"] == "Amitava Chatterjee":
        driver.find_element(By.XPATH, '//option[@value="177909"]').click()
    elif row["Class Taken By"] == "Manjima Saha":
        driver.find_element(By.XPATH, '//option[@value="176763"]').click()
    elif row["Class Taken By"] == "Sujata Ghatak":
        driver.find_element(By.XPATH, '//option[@value="179676"]').click()

    driver.execute_script('document.getElementById("date_tme").removeAttribute("readonly")')
    driver.find_element(By.XPATH, '//input[@id="date_tme"]').click()
    sleep(1)
    elem = driver.find_element(By.XPATH, '//input[@id="date_tme"]')
    ac.move_to_element(elem).move_by_offset(213, 10).click().perform()
    sleep(1)
    driver.find_element(By.XPATH, '//input[@id="date_tme"]').send_keys("fuck you")
