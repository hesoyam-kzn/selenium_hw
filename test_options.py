import time, pytest, math
from selenium import webdriver
from selenium.webdriver.common.by import By


# @pytest.fixture()
# def get_browser(self):

answer = math.log(int(time.time()))
link = 'https://stepik.org/lesson/236895/step/1'
seq = (str(a) for a in [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])

@pytest.mark.parametrize("lnk", seq)
def test_options(browser, lnk):
# browser = webdriver.Chrome()
    browser.get(f'https://stepik.org/lesson/{lnk}/step/1')
    browser.implicitly_wait(5)

    #Authorization
    browser.find_element(By.CLASS_NAME, 'ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button').click()
    browser.find_element(By.CSS_SELECTOR, '.ember-text-field.ember-view.sign-form__input[type="email"]').send_keys('dimaswat@gmail.com')
    browser.find_element(By.CSS_SELECTOR, '.ember-text-field.ember-view.sign-form__input[type="password"]').send_keys('@Lvbnhbq397')
    browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader').click()

    time.sleep(5)
    text_f = browser.find_element(By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea')
    text_f.send_keys(str(answer))
    # time.sleep(100)
    # browser.find_element(By.CLASS_NAME, 'attempt-wrapper-button').click()




# browser.quit()