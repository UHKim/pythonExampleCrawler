import os
from selenium import webdriver
from bs4 import BeautifulSoup

print(os.environ['PATH_CHROMEDRIVER'])

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(
    os.environ['PATH_CHROMEDRIVER'], options=options)

driver.get(
    "http://www.leopold.co.kr/?doc=bbs/gnuboard.php&bo_table=notice")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

lists = soup.findAll("span", {"class": "tt"})

for listElem in lists:
    if 'FC900R' in listElem.text:
        print(listElem.text)
