from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby_h3 = driver.find_element(By.XPATH, '//h3[text() = "Selenium Ruby"]')
selenium_ruby_h3.click()
time.sleep(2)
reviews_button = driver.find_element(By.CLASS_NAME, 'reviews_tab')
reviews_button.click()
time.sleep(2)
five_stars = driver.find_element(By.CLASS_NAME, 'star-5')
five_stars.click()
time.sleep(2)
textarea = driver.find_element(By.ID, 'comment')
textarea.send_keys('Nice Book!')
time.sleep(2)
input_name = driver.find_element(By.ID, 'author')
input_name.send_keys('Vasya')
time.sleep(2)
input_email = driver.find_element(By.ID, 'email')
input_email.send_keys('Vasya@mail.ru')
time.sleep(2)
submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()
time.sleep(2)
driver.close()