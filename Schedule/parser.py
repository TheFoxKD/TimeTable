#  Copyright (c) 2021. TheFox
import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

DEBUG = False  # режим Debug, в конечном проекте использовать значение False
TIME_SLEEP = 3  # время сна перед действиями
CHROME_BASE = os.getcwd()
settings = webdriver.ChromeOptions()
if not DEBUG:
    settings.add_argument('headless')  # аргумент отвечает за запуск окна в скрытом режиме
driver = webdriver.Chrome(options=settings, executable_path=os.path.join(CHROME_BASE, 'chromedriver.exe'))
driver.maximize_window()
driver.get("https://giseo.rkomi.ru/about.html")

# Для даунов, это данные для входа в гисео

data = []


def date_reformat(date_old):
    """
    Функция обработки даты, реформат месяца.
    :param date_old: дата старого формата (буквами) типа string
    :return: дата нвого формата (порядковым номером) типа string
    """
    if date_old.find('янв') > 0:
        month = '01'
    elif date_old.find('февр') > 0:
        month = '02'
    elif date_old.find('мар') > 0:
        month = '03'
    elif date_old.find('апр') > 0:
        month = '04'
    elif date_old.find('мая') > 0:
        month = '05'
    elif date_old.find('июня') > 0:
        month = '06'
    elif date_old.find('июля') > 0:
        month = '07'
    elif date_old.find('авг') > 0:
        month = '08'
    elif date_old.find('сент') > 0:
        month = '09'
    elif date_old.find('окт') > 0:
        month = '10'
    elif date_old.find('нояб') > 0:
        month = '11'
    elif date_old.find('дек') > 0:
        month = '12'
    return month


def parse_html(html):
    """
    Парсинг страницы ЭД, получение необходимых данных, их преобразование и запись в список.
    :param html: код старницы, принимаемый из функции parsing() формат string
    :return: возврат данных в формате list, каждый элемент dict содержит название предмета, дату, ДЗ, время окончания
    и время начала.
    ПРИМЕР ВОЗВРАЩАЕМЫХ ДАННЫХ:
        [{'affair': 'Физическая культура',
        'date': '2021-12-20',
        'homework': '',
        'time_end': '14:00:00',
        'time_start': '13:20:00'},
        {'affair': 'Технология',
        'date': '2021-12-20',
        'homework': 'Повторить записи в тетради',
        'time_end': '14:50:00',
        'time_start': '14:10:00'}]
    """
    if DEBUG:
        print(html)
    soup = BeautifulSoup(html, 'html5lib')
    days = soup.find_all('div', class_='day_table')
    if DEBUG:
        print(len(days))
    for y in range(len(days)):
        date = days[y].find('span', class_='ng-binding').text
        if DEBUG:
            print(date)
        work = days[y].find_all('tr', class_='ng-scope')
        year = date[-7:-3]
        day_ = date[4:6].replace(' ', '')
        if len(day_) == 1:
            day_ = "0" + day_
        month = date_reformat(date)
        # print(month)
        # print(date)
        date_fin = f'{year}-{month}-{day_}'
        for i in range(len(work)):
            les = work[i].find_all('td')[1]
            name_les = les.find('a')
            if name_les is not None:
                hw = work[i].find('a', class_='ng-binding ng-scope')
                if hw is not None:
                    hw = hw.text
                else:
                    hw = ''
                if DEBUG:
                    print(name_les)
                time_start = str(les.find('div').text[:5]) + ':00'
                time_finish = str(les.find('div').text[8:13]) + ':00'
                if DEBUG:
                    print(f'{date_fin} {name_les.text}   start: {time_start} finish: {time_finish} HW: {hw}')
                data_local = {'date': date_fin, 'affair': name_les.text, 'homework': hw, 'time_end': time_finish,
                              'time_start': time_start}
                data.append(data_local)
    return data


def parsing(place, town, type_school, school, login, password):
    """
    Ввод данных пользователя и вход в ЭД, парсинг кода всей страницы.
    :param place: район
    :param town: город
    :param type_school: тип ОО
    :param school: номер школы/название
    :param login: логин из ЭД
    :param password: пароль из ЭД
    :return: html код старницы ЭЛ дневника
    """
    driver.get("https://giseo.rkomi.ru/about.html")
    time.sleep(TIME_SLEEP)
    try:
        in_place = Select(driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div/select'))
        in_place.select_by_visible_text(place)
        in_town = Select(driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[4]/div/select'))
        in_town.select_by_visible_text(town)
    except:
        pass

    in_type_school = Select(
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[5]/div/select'))
    in_type_school.select_by_visible_text(type_school)
    try:
        in_school = Select(driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[6]/div/select'))
        in_school.select_by_visible_text(school)
    except:
        pass
    in_login = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[8]/input')
    in_login.send_keys(login)
    in_password = driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[9]/input')
    in_password.send_keys(password)
    sing_in = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[12]/a/span')
    # sing_in.click()
    driver.execute_script("arguments[0].click();", sing_in)
    time.sleep(TIME_SLEEP)
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div/div[4]/div/div/div/div/button[2]/span[2]').click()
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
    time.sleep(TIME_SLEEP)

    diary = driver.find_element_by_xpath('/html/body/div[1]/div[4]/nav/ul/li[4]/a')
    but = driver.find_element_by_xpath('/html/body/div[1]/div[4]/nav/ul/li[4]/ul/li[1]/a')

    Hover = ActionChains(driver).move_to_element(diary)
    Hover.perform()
    but.click()
    # driver.find_element_by_xpath(
    #    '/html/body/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/i').click()
    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # driver.implicitly_wait(5)
    time.sleep(TIME_SLEEP)
    # print(driver.current_url)
    html = driver.page_source
    # print(html)

    return parse_html(html)


if __name__ == "__main__":
    """
    Режим тестирования, запуск файла "вручную" запустит этот код и проведет тест с принимаяемыми значениями,
    которые описаны ниже.
    """
    time.sleep(TIME_SLEEP)
    # parsing(place='Городской округ Сыктывкар', town='Сыктывкар, г.', type_school='Общеобразовательная', school='МАОУ "Технологический лицей"', login='Криштопа', password='576789')
    driver.quit()
