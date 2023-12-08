from selenium import webdriver
from selenium.webdriver.common.by import By


def login(driver):
    my_account_button = driver.find_element(By.LINK_TEXT, 'My Account')
    my_account_button.click()
    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys('vasya-pupkin@mail.ru')
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys('123adfs#*FSDF')
    login_button = driver.find_element(By.NAME, 'login')
    login_button.click()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://practice.automationtesting.in/')
    login(driver)
    driver.close()