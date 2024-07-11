from playwright.sync_api import sync_playwright
from playwright.devices import devices

def run(playwright):
    device = devices['iPhone 11']
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(**device) # Запуск браузера в видимом режиме
    page = browser.new_page()

    context.set_geolocation(latitude=55.7558, longitude=37.6173)    
    # Переходим на страницу объявления
    page.goto('https://krisha.kz/a/show/694624940')  # Замените 123456 на реальный номер объявления

    # Ждем, пока элемент с телефоном не станет доступен (предполагая, что такой элемент есть)
    page.wait_for_selector('button.show-phones')

    page.click('button.show-phones')
    # Считываем номер телефона
    page.wait_for_selector('div.offer__contacts-phones')
    
    phone_number = page.inner_text('div.offer__contacts-phones')  # Селектор для номера телефона
    print(f'Номер телефона: {phone_number}')

    # Закрываем браузер
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
