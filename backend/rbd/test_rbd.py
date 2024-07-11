from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import re
import time
from selenium.common.exceptions import NoSuchElementException

# Инициализация драйвера
driver = webdriver.Chrome()
#на будущее
# chrome_options = Options()
# chrome_options.add_argument("--start-fullscreen")  # Запуск Chrome в полноэкранном режиме

# # Инициализация драйвера с заданными опциями
# driver = webdriver.Chrome(options=chrome_options)

# Функция для получения данных по каждому объекту


try:
    # Вход на сайт
    driver.get('https://rbd.kz/site/login')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.rb-email')))
    driver.find_element(By.CSS_SELECTOR, 'input.rb-email').send_keys('siko.mukhametalin@gmail.com')
    driver.find_element(By.CSS_SELECTOR, 'input.rb-password').send_keys('270299SMDlove!123456789012')
    driver.find_element(By.CSS_SELECTOR, 'button.btn-login').click()

    # Переход на страницу с объектами
    WebDriverWait(driver, 10).until(lambda d: d.current_url != 'https://rbd.kz/site/login')
    # на будущее 
    # driver.get('https://rbd.kz/app/demand/recent')
#         time.sleep(10)

#     search_button = driver.find_element(By.CSS_SELECTOR, ".btn.v-btn-search.rb-btn-search.btn-success")

#     print(f"search_button -------------- {search_button}")

# # Клик по кнопке, если это необходимо
#     search_button.click()

    driver.get('https://rbd.kz/app/demand/start/13057143')


    # Ожидание загрузки страницы
    while True:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody")))

        # Получение всех кнопок для перехода к деталям объектов
        tbody = driver.find_element(By.CSS_SELECTOR, "tbody[role='rowgroup']")

        # Получаем все строки внутри найденного tbody
        tr_elements = tbody.find_elements(By.TAG_NAME, 'tr')

        print(f"tr_elements --------- {tr_elements}")

        # Собираем данные из каждой строки
        
        rows = {}
        for tr in tr_elements:
            tr.click()
            time.sleep(5)
            slider_bar = driver.find_element(By.ID, "rb-supply-show-permanent")
            price = slider_bar.find_element(By.CSS_SELECTOR,'a.rb-regular-price')
            rows['price'] = price.text
            print(f"price -------{price.text}")

            photo = []
            photo_html = slider_bar.find_elements(By.CSS_SELECTOR, "div.main.async-image.rb-photo")
            print(f"photo_html ----------- {photo_html}")
            for ph in photo_html:
                temp_photo_html = (ph.find_element(By.CSS_SELECTOR,'span.rb-inner.rb-cover'))
                style_photo_attribute =  temp_photo_html.get_attribute('style')
                photo.append(re.search(r'url\("([^"]+)"\)', style_photo_attribute).group(1))
            print(f"photo ----------- {photo}")
            rows['photo_url'] = photo

            adress_html = slider_bar.find_element(By.CSS_SELECTOR, 'div.rb-address-text')
            rows['adress_html'] = adress_html.text
            print(f"adress - {adress_html.text}")

            main_info_html = slider_bar.find_element(By.CSS_SELECTOR,'div.rb-inner')
            all_info_html  = main_info_html.find_elements(By.CSS_SELECTOR,'span.rb-value')
            x = 0
            for info in all_info_html:
                x += 1

                if(x == 1):
                    rows['id'] = info.text
                elif(x == 2):
                    rows['count_room'] = info.text
                elif(x == 3):
                    rows['area'] = info.text
                elif(x == 4):
                    rows['floor'] = info.text
                elif(x == 5):
                    rows['all_floor'] = info.text
                elif(x == 6):
                    rows['remont'] = info.text
                elif(x == 7):
                    rows['years'] = info.text
                elif(x == 8):
                    rows['height'] = info.text
                elif(x == 9):
                    rows['privat_obshaga'] = info.text
                else:
                    rows['in_zalog'] = info.text




            button_closed_slidebar = driver.find_element(By.CSS_SELECTOR, ".btn.rb-close-sidebar.btn-icon.btn-plain")
            button_closed_slidebar.click()

        right_arrow = driver.find_element(By.CSS_SELECTOR, "li.controll.rb-visible:not(.disabled) > a.page-link.right")
        right_arrow.click()  # Кликаем по стрелке
        time.sleep(2) 
            


    # Конвертируем список словарей в JSON
    json_data = json.dumps(rows, ensure_ascii=False, indent=4)

    # Запись JSON в файл
    with open('output.json', 'w', encoding='utf-8') as f:
        f.write(json_data)

    # Выводим путь к файлу
    print("Data has been written to output.json")

except Exception as error:
    print(f"error ------- {error}")

driver.quit()

# Вывод информации
# for detail in all_details:
#     print(detail)
