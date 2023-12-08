from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login
import time
driver = webdriver.Chrome()
driver_wait = WebDriverWait(driver, 5)
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')
login(driver)
    # Отображение страницы товара
shop_link = driver.find_element(By.LINK_TEXT, 'Shop')
shop_link.click()
html_5_forms = driver.find_element(By.CSS_SELECTOR, '.post-181 > a:nth-child(1)')
html_5_forms.click()
if driver.find_element(By.TAG_NAME, 'h1').text == 'HTML5 Forms':
    print('y')
else:
    print('n')
    # #Количество товаров в категории
shop_link = driver.find_element(By.LINK_TEXT, 'Shop')
shop_link.click()
html_link = driver.find_element(By.LINK_TEXT, 'HTML')
html_link.click()
goods_list = driver.find_elements(By.CSS_SELECTOR, '.products > li')
if len(goods_list) == 3:
    print('y')
else:
    print('n')
    # Сортировка товаров
shop_link = driver.find_element(By.LINK_TEXT, 'Shop')
shop_link.click()
selector = driver.find_element(By.CLASS_NAME, 'orderby')
selector.click()
option_selected = driver.find_element(By.CSS_SELECTOR, 'select > [value="menu_order"]').get_attribute('selected')
if option_selected:
    print('y')
else:
    print('n')
select = Select(selector)
select.select_by_value('price-desc')
selector = driver.find_element(By.CLASS_NAME, 'orderby')
selector.click()
option_selected = driver.find_element(By.CSS_SELECTOR, 'select > [value="price-desc"]').get_attribute('selected')
if option_selected:
    print('y')
else:
    print('n')
    # Отображение, скидка товара
shop_link = driver.find_element(By.LINK_TEXT, 'Shop')
shop_link.click()
android_book = driver.find_element(By.CSS_SELECTOR, '.post-169 > a:nth-child(1)')
android_book.click()
old_price = driver.find_element(By.CSS_SELECTOR, '.price del > span').text
if old_price == '₹600.00':
    print('y')
else:
    print('n')
new_price = driver.find_element(By.CSS_SELECTOR, '.price ins > span').text
if new_price == '₹450.00':
    print('y')
else:
    print('n')
book_image = driver.find_element(By.CSS_SELECTOR, '.images > a')
book_image.click()
driver_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
cross_button = driver.find_element(By.CLASS_NAME, 'pp_close')
cross_button.click()
    # Проверка цены в корзине
shop_link = driver.find_element(By.LINK_TEXT, 'Shop')
shop_link.click()
add_to_basket_button = driver.find_element(By.CSS_SELECTOR, '.post-169 > a:nth-child(2)')
add_to_basket_button.click()
driver_wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'cartcontents'), '1 Item'))
driver_wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.wpmenucartli .amount'), '₹450.00'))
items_count = driver.find_element(By.CLASS_NAME, 'cartcontents').text
assert items_count == '1 Item'
price = driver.find_element(By.CSS_SELECTOR, '.wpmenucartli .amount').text
assert price == '₹450.00'
basket = driver.find_element(By.CLASS_NAME, 'wpmenucart-contents')
basket.click()
driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-subtotal .amount')))
driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.order-total .amount')))
    # Работа в корзине
shop_link = driver.find_element(By.LINK_TEXT, 'Shop')
shop_link.click()
driver.execute_script('window.scrollBy(0, 300);')
add_to_basket_button = driver.find_element(By.CSS_SELECTOR, '.post-182 > a:nth-child(2)')
add_to_basket_button.click()
time.sleep(0.5)
add_to_basket_button = driver.find_element(By.CSS_SELECTOR, '.post-180 > a:nth-child(2)')
add_to_basket_button.click()
basket = driver.find_element(By.CLASS_NAME, 'wpmenucart-contents')
basket.click()
cross_button = driver.find_element(By.CSS_SELECTOR, 'tbody > .cart_item:nth-child(1) .product-remove > a')
cross_button.click()
driver_wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Undo?')))
undo = driver.find_element(By.LINK_TEXT, 'Undo?')
undo.click()
quantity_input = driver.find_element(By.CSS_SELECTOR, 'tbody > .cart_item:nth-child(2) .quantity > input')
quantity_input.clear()
quantity_input.send_keys('3')
update_basket_button = driver.find_element(By.NAME, 'update_cart')
update_basket_button.click()
quantity_input_value = driver.find_element(By.CSS_SELECTOR, 'tbody > .cart_item:nth-child(2) .quantity > input').get_attribute('value')
assert quantity_input_value == '3'
time.sleep(1)
apply_button = driver.find_element(By.NAME, 'apply_coupon')
apply_button.click()
driver_wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-error > li'), 'Please enter a coupon code.'))
print("Текст 'Please enter a coupon code.'")
    # Покупка товара
shop_link = driver.find_element(By.LINK_TEXT, 'Shop')
shop_link.click()
driver.execute_script('window.scrollBy(0, 300);')
add_to_basket_button = driver.find_element(By.CSS_SELECTOR, '.post-182 > a:nth-child(2)')
add_to_basket_button.click()
driver_wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'cartcontents'), '1 Item'))
basket = driver.find_element(By.CLASS_NAME, 'wpmenucart-contents')
basket.click()
driver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.wc-proceed-to-checkout > a')))
proceed_button = driver.find_element(By.CSS_SELECTOR, '.wc-proceed-to-checkout > a')
proceed_button.click()
fist_name_input = driver.find_element(By.ID, 'billing_first_name')
fist_name_input.send_keys('Vasiliy')
country_selector = driver.find_element(By.CLASS_NAME, 'select2-choice')
country_selector.click()
country_input = driver.find_element(By.ID, 's2id_autogen1_search')
country_input.send_keys('russia')
option = driver.find_element(By.CLASS_NAME, 'select2-result-label')
option.click()
driver.execute_script('window.scrollBy(0, 600);')
time.sleep(0.5)
place_order_button = driver.find_element(By.ID, 'place_order')
place_order_button.click()
driver.close()
