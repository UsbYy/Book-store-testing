from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')
my_account_button = driver.find_element(By.LINK_TEXT, 'My Account')
my_account_button.click()
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys('vasya-pupkin@mail.ru')
password_input = driver.find_element(By.ID, 'reg_password')
password_input.send_keys('123adfs#*FSDF')
register_button = driver.find_element(By.NAME, 'register')
register_button.click()
driver.close()



