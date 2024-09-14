from selenium import webdriver
import pytest
from datetime import datetime, timedelta


# Создаем фикстуру которая будет настраивать наш браузер 
@pytest.fixture() 
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.set_window_size(1920, 1080)
    chrome_browser.implicitly_wait(20)
    return chrome_browser

@pytest.fixture()
def date_number():
    # Получаем текущею дату и увеличиваем ее на количество дней
    number_date = datetime.now() + timedelta(days=7)
    # Трансформируем дату в нужный нам вид 
    number_date = number_date.strftime("%d.%m.%Y") 
    return number_date


@pytest.fixture()
def date_years():
    number_date = datetime.now() + timedelta(days=7)
    # Получаем текущий год и увеличиваем на количество лет
    new_date = int(datetime.now().strftime("%Y")) + 20
    current_date = number_date.strftime("%d.%m." + str(new_date))
    return current_date