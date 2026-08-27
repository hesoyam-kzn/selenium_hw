import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(5)

prc = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
browser.find_element(By.ID, 'book').click()
x = int(browser.find_element(By.ID, 'input_value').text)
form = str(log(abs(12*sin(x))))
print(f'form = {form}')
formm = browser.find_element(By.ID, 'answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", formm)
print(formm)
formm.send_keys(form)
btn = browser.find_element(By.ID, 'solve')
btn.click()

time.sleep(10)




