# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

driver = webdriver.Chrome()
fix = 'https://fix-online.sbis.ru/'
user_login = 'asus'
user_password = 'asus43210'
user_name = 'Сергеев Сергей'
message = 'Шалом!'

try:
    driver.get(fix)
    driver.maximize_window()
    sleep(1)

    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)

    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)

    contacts_accordion = driver.find_element(By.CSS_SELECTOR, '[data-name="contacts"]')
    contacts_accordion.click()

    contacts = driver.find_element(By.CSS_SELECTOR, '[name="headTitle"]')
    contacts.click()
    sleep(1)

    add_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    add_btn.click()

    search = driver.find_element(By.XPATH, '//*[@id="popup"]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/input')
    search.send_keys(user_name)
    sleep(1)

    addressee = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    addressee.click()
    sleep(1)

    text_input_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    text_input_field.send_keys(message)

    send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_btn.click()
    sleep(1)

    message_field = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text p')
    assert message_field.text == message, 'Сообщение не соответствует введеному'

    actions = ActionChains(driver)
    actions.context_click(message_field)
    actions.perform()
    sleep(1)

    delete_btn = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    delete_btn.click()
    sleep(1)

    message_field = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text p')
    assert message_field.text != message, 'Сообщение не удалено'

finally:
    driver.quit()