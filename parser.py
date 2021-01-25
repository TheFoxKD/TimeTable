from selenium import webdriver
from selenium.webdriver.support.ui import Select
settings = webdriver.ChromeOptions()
# settings.add_argument('headless')
driver = webdriver.Chrome()
driver.get("https://giseo.rkomi.ru/about.html")

place = 'Городской округ Сыктывкар'
town = 'Сыктывкар, г.'
type_school = 'Общеобразовательная'
school = 'МАОУ "Технологический лицей"'
login = 'СухановА2'
password = '290483'


def parsing(place, town, type_school, school, login, password):
    if place.find('городской'):
        pass
    else:
        select_town = Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[4]/div/select'))
        select_town.deselect_by_visible_text(town)
        print('reew')
    select_place = Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div/select'))
    select_type_school = Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[5]/div/select'))
    select_school = Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[6]/div/select'))
    input_login = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[8]/input')
    input_password = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[8]/input')
    input_login.send_keys(login)
    input_password.send_keys(password)
    select_school.deselect_by_visible_text(school)
    select_type_school.deselect_by_visible_text(type_school)
    select_place.deselect_by_visible_text(place)

parsing(place, town, type_school, school, login, password)
