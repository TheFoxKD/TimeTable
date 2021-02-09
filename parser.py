from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

settings = webdriver.ChromeOptions()
settings.add_argument('headless')
driver = webdriver.Chrome()
driver.get("https://giseo.rkomi.ru/about.html")

place = 'Городской округ Сыктывкар'
town = 'Сыктывкар, г.'
type_school = 'Общеобразовательная'
school = 'МАОУ "Технологический лицей"'
login = 'СухановА2'
password = '290483'


def parse_html(html):
    print(html)
    soup = BeautifulSoup(html, 'html5lib')
    days = soup.find_all('div', class_='day_table')
    print(days)
    for day in days:
        print(day. find('span', class_='ng-binding').text)

def parsing(place, town, type_school, school, login, password):
    in_place = Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div/select'))
    in_place.select_by_visible_text(place)
    try:
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


    #--------------------------------------------------------------------------------------------------------------------------------------------

    diary = driver.find_element_by_xpath('/html/body/div[1]/div[4]/nav/ul/li[4]/a')
    but = driver.find_element_by_xpath('/html/body/div[1]/div[4]/nav/ul/li[4]/ul/li[1]/a')

    Hover = ActionChains(driver).move_to_element(diary)
    Hover.perform()
    but.click()

    #---------------------------------------------------------------------------------------------------------------------------------------------
    # driver.implicitly_wait(5)
    time.sleep(2)
    print(driver.current_url)
    html = driver.page_source
    parse_html(html)



parsing(place, town, type_school, school, login, password)

driver.quit()