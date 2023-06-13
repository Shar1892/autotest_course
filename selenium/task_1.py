# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

sbis_site = "https://sbis.ru/"

try:
    driver.get(sbis_site)
    driver.maximize_window()
    sleep(2)

    contacts = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    contacts.click()
    sleep(2)

    logo = driver.find_element(By.CSS_SELECTOR, '[title="tensor.ru"]')
    logo.click()

    driver.switch_to.window(driver.window_handles[1])
    sleep(2)

    news_block = driver.find_element(By.CSS_SELECTOR, '[class="tensor_ru-Index__block4-content tensor_ru-Index__card"]')
    assert news_block.is_displayed(), 'Нет блока Сила в людях'

    more_link = driver.find_element(By.CSS_SELECTOR, 'p [href="/about"]')
    driver.execute_script('return arguments[0].scrollIntoView(true);', more_link)
    more_link.click()
    sleep(1)

    assert driver.current_url == "https://tensor.ru/about"

finally:
    driver.quit()
