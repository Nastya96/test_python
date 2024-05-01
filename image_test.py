from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    return browser

#test_1
def test_photos_dimensions(driver):

    driver.get("https://sbis.ru/")

    #Перейти  в раздел Контакты, найти баннер Тензор
    driver.find_element(By.LINK_TEXT, "Контакты").click()
    driver.find_element(By.CLASS_NAME, 'sbisru-Contacts__logo-tensor').click()
    driver.get("https://tensor.ru/")
    time.sleep(20)
    # Проверить, что есть блок "Сила в людях"
    driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div/div[5]/div/div/div[1]/div/p[1]")
    #Подробнее
    driver.find_element(By.XPATH, "//*[ @ id = 'container']/div[1]/div/div[5]/div/div/ div[1] / div / p[4] / a ")
    #driver.find_element(By.XPATH, "// *[ @ id = 'container'] / div[1] / div / div[5] / div / div / div[1] / div / p[4] / a ").click()
    driver.get("https://tensor.ru/about")
    time.sleep(10)
    image_element_1 = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img')
    image_element_2 = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img')
    image_element_3 = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img')
    image_element_4 = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img')

    width = []
    height = []

    width.append(image_element_1.size['width'])
    width.append(image_element_2.size['width'])
    width.append(image_element_3.size['width'])
    width.append(image_element_4.size['width'])

    height.append(image_element_1.size['height'])
    height.append(image_element_2.size['height'])
    height.append(image_element_3.size['height'])
    height.append(image_element_4.size['height'])

    if len(set(width)) == 1:
        set1 = 'images have the same width'
    else:
        set1 = 'images have the different width'

    if len(set(height)) == 1:
        set2 = 'images have the same heigth'
    else:
        set2 = 'images have the different heigth'

    if set1 == 'images have the same width' and set2 == 'images have the same heigth':
        test_message = 'images have same size'
    else:
        test_message = 'images different size'

    assert test_message == 'images have same size'


def test_list(driver):
    driver.get("https://sbis.ru/")
    driver.find_element(By.LINK_TEXT, "Контакты").click()
    time.sleep(10)
    assert driver.current_url == "https://sbis.ru/contacts/52-nizhegorodskaya-oblast?tab=clients"
    partners = driver.find_element(By.ID, "contacts_list")
    assert partners is not None, "Нет списка партнеров"
    driver.find_element(By.CLASS_NAME, 'sbis_ru-Region-Chooser__text').click()  # Клик на меню выбора региона
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, '[title="Камчатский край"]').click()  # Клик на "Камчатский край"
    time.sleep(10)
    assert driver.current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"


