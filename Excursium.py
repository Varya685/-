from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Переход на страницу (исправленный URL)
    driver.get('https://excursium.com/')

    # Ожидание и поиск поля email
    wait = WebDriverWait(driver, 10)
    email_input = wait.until(
        EC.element_to_be_clickable((By.NAME, 'email'))
    )
    # Ввод текста в поле email
    email_input.send_keys('strizhova.varya@gmail.com')

    # Поиск поля пароля
    password_input = wait.until(
        EC.element_to_be_clickable((By.NAME, 'password'))
    )
    # Ввод пароля
    password_input.send_keys('123456')

    # Поиск кнопки входа
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, 'login-btn'))  
    )
    # Клик по кнопке
    login_button.click()

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие драйвера в блоке finally — выполняется всегда
    driver.quit()
