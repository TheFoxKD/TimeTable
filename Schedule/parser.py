#  Copyright (c) 2021. TheFox

import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


# Это настройки, не трогай их, если ты не дибил
time_sleep = 3
settings = webdriver.ChromeOptions()
settings.add_argument('headless')
driver = webdriver.Chrome(options=settings, executable_path=r"/home/artem/PycharmProjects/TimeTable/chromedriver")
driver.maximize_window()
driver.get("https://giseo.rkomi.ru/about.html")

# Для даунов, это данные для входа в гисео

data = {}
time.sleep(time_sleep)

def parse_html(html):
    """
    В этой функции царствует bs4 здесь идет парсинг основных данных.
    Итоговые значения записанны в data (type - dict), ключи с названиями из бд и в таком же порядке.
    """
    # print(html)
    soup = BeautifulSoup(html, 'html5lib')
    days = soup.find_all('div', class_='day_table')
    # print(days)
    for day in days:
        date = day.find('span', class_='ng-binding').text
        work = day.find_all('tr', class_='ng-scope')
        year = date[-7:-3]
        day_ = date[4:6]
        if date.find('янв'):
            month = '01'
        if date.find('фев'):
            month = '02'
        if date.find('март'):
            month = '03'
        if date.find('апр'):
            month = '04'
        if date.find('мая'):
            month = '05'
        if date.find('июн'):
            month = '06'
        if date.find('июл'):
            month = '07'
        if date.find('авг'):
            month = '08'
        if date.find('сен'):
            month = '09'
        if date.find('окт'):
            month = '10'
        if date.find('ноя'):
            month = '11'
        if date.find('дек'):
            month = '12'
        date_fin = f'{year}-{month}-{day_}'

        for i in range(len(work)):
            les = work[i].find_all('td')[1]
            name_les = les.find('a')
            if name_les != None:
                hw = work[i].find('a', class_='ng-binding ng-scope')
                if hw != None:
                    hw = hw.text
                else:
                    hw = ''
                time_start = str(les.find('div').text[:5]) + ':00'
                time_finish = str(les.find('div').text[8:13]) + ':00'
                # print(f'{name_les.text}   start: {time_start} finish: {time_finish} HW: {hw}')
                data_local = {'date': date_fin, 'affair': name_les.text, 'homework': hw, 'time_end': time_finish, 'time_start': time_start}
                data[i] = data_local
    return data


def parsing(place, town, type_school, school, login, password):
    try:
        in_place = Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div/select'))
        in_place.select_by_visible_text(place)
        in_town = Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[4]/div/select'))
        in_town.select_by_visible_text(town)
    except:
        pass
    in_type_school = Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[5]/div/select'))
    in_type_school.select_by_visible_text(type_school)
    try:
        in_school = Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[6]/div/select'))
        in_school.select_by_visible_text(school)
    except:
        pass
    in_login = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[8]/input')
    in_login.send_keys(login)
    in_password = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[9]/input')
    in_password.send_keys(password)
    sing_in = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[12]/a/span')
    sing_in.click()
    driver.implicitly_wait(5)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[4]/div/div/div/div/button[2]/span[2]').click()
    except:
        print('error')
        pass
    # print(driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div/div').text())
    #
    # try:
    #     driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[4]/div/div/div/div/button[2]').click()
    # except:
    #     pass

    # --------------------------------------------------------------------------------------------------------------------------------------------

    diary = driver.find_element_by_xpath('/html/body/div[1]/div[4]/nav/ul/li[4]/a')
    but = driver.find_element_by_xpath('/html/body/div[1]/div[4]/nav/ul/li[4]/ul/li[1]/a')

    Hover = ActionChains(driver).move_to_element(diary)
    Hover.perform()
    but.click()

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # driver.implicitly_wait(5)
    time.sleep(time_sleep)
    # print(driver.current_url)
    html = driver.page_source
    return parse_html(html)



# СМТОРИ СЮДА, КУСОК ГОВНА!!! Вот это ↑ ↑ ↑ - основная функция, её нужно вызывать с этими данными входа,
# но чтоюы их получить мне нужен user_id его у меня нет так же, как и доступа к моделям, поэтому добавить
# данные после парсинга я не могу в бд, дебил. Данные после парсинга нужно

# Это лять для того, чтобы твоя захудалая оперативка не охренела от вкладок в хроме
# driver.quit()
