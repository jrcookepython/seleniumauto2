import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tkinter import *
import time
import csv

#CONSTANTS
URL = 'https://jeff-blog.herokuapp.com/'
HEADING_IMAGE = '/html/body/header'
TIMEOUT = 30
REGISTER_BUTTON = '/html/body/nav/div/div/ul/li[3]/a'
HOME_BUTTON = '//*[@id="navbarResponsive"]/ul/li[1]/a'

#USING SELENIUM DRIVER TO OPEN BROWSER
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()

#GET HEADER INGO
header_image_wait = expected_conditions.presence_of_element_located((By.XPATH, HEADING_IMAGE))
WebDriverWait(driver, TIMEOUT).until(header_image_wait)

header_image_path = driver.find_element(by=By.XPATH, value=HEADING_IMAGE)
image_url = header_image_path.get_attribute('style')
header_text = header_image_path.text

print(image_url)
print(header_text)


#GETTING POST TITLES
data_scrape = []

for post in range(0, 2):
    post_path_wait = expected_conditions.presence_of_element_located((By.XPATH, f'/html/body/div/div/div/div[{int(post)+1}]/a/h2'))
    WebDriverWait(driver, TIMEOUT).until(post_path_wait)

    post_path_available = driver.find_element(by=By.XPATH, value=f'/html/body/div/div/div/div[{int(post)+1}]/a/h2')
    post_title = post_path_available.text
    print(f"Header {int(post+1)} is {post_title}.")
    data_scrape.append(post_title)

print(data_scrape)

#GETTING POST IMAGES

post_images = []
for post_data in range(0, 2):
    post_path_wait = expected_conditions.presence_of_element_located((By.XPATH, f'/html/body/div/div/div/div[{int(post_data) + 1}]/a/h2'))
    WebDriverWait(driver, TIMEOUT).until(post_path_wait)

    post_path_available = driver.find_element(by=By.XPATH, value=f'/html/body/div/div/div/div[{int(post_data)+1}]/a/h2')
    post_path_available.click()

    post_header_image_click = expected_conditions.presence_of_element_located((By.XPATH, f"/html/body/header"))
    WebDriverWait(driver, TIMEOUT).until(post_header_image_click)

    post_header_image = driver.find_element(by=By.XPATH, value='/html/body/header')
    post_header_image_attribute =  post_header_image.get_attribute('style')
    post_images.append(post_header_image_attribute)

    home_button_find = expected_conditions.presence_of_element_located((By.XPATH, HOME_BUTTON))
    WebDriverWait(driver, TIMEOUT).until(home_button_find)

    home_button_clickable = driver.find_element(by=By.XPATH, value='//*[@id="navbarResponsive"]/ul/li[1]/a')
    home_button_clickable.click()

print(post_images)

#IMPORT POST IMAGES DATA INTO CSV FILE

reader = csv.reader(post_images)

with open('test.csv', 'a') as file:
    for images in range(0, len(post_images)):
        writer = csv.writer(file)
        writer.writerows(list(reader))
