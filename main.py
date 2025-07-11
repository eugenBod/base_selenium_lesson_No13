import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# Создаем настройки браузера
options = webdriver.ChromeOptions()

# Предотвращаем закрытие браузера после выполнения скрипта
options.add_experimental_option("detach", True)

# Запускаем Chrome с автоматически установленным драйвером и заданными опциями
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Базовые данные
base_url = "http://www.saucedemo.com/"
valid_username = "performance_glitch_user"
valid_password = "secret_sauce"
invalid_username = "user12345"
invalid_password = "password12345"

# Переход на страницу авторизации  и разворачивание окна на весь экран
driver.get(base_url)
driver.maximize_window()

# Ввод неверного логина, выделение и удаление
time.sleep(1)
username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
username_field.send_keys(invalid_username)
print("Input incorrect login")

time.sleep(1)
username_field.send_keys(Keys.CONTROL + "a")
print("Incorrect login highlight")

time.sleep(1)
username_field.send_keys(Keys.DELETE)
print("Incorrect login deleted")

# Ввод неверного пароля, выделение и удаление
time.sleep(1)
password_field = driver.find_element(By.XPATH, "//input[@id='password']")
password_field.send_keys(invalid_password)
print("Input incorrect password")

time.sleep(1)
password_field.send_keys(Keys.CONTROL + "a")
print("Incorrect password highlight")

time.sleep(1)
password_field.send_keys(Keys.DELETE)
print("Incorrect password deleted")

# Ввод логина
time.sleep(1)
username_field.send_keys(valid_username)
print("Input login")

# Ввод пароля
time.sleep(1)
password_field.send_keys(valid_password)
print("Input password")

# Клик по кнопке "Login"
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
print("Click login button")

# Выход из браузера
time.sleep(1)
driver.quit()
print("Browser is closed")