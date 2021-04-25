from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 
import datetime

url_mockaroo = ('https://dados.gov.br/')

site_dadosgov = webdriver.Chrome()
site_dadosgov.get(url_mockaroo)

site_dadosgov.find_element_by_xpath('//*[@id="menu-horizontal"]/ul/li[1]/a').click()
sleep(2)
site_dadosgov.find_element_by_xpath('//*[@id="content"]/div[3]/aside/div/div/section[2]/nav/ul/li[2]/a/span').click()
sleep(2)
site_dadosgov.find_element_by_xpath('//*[@id="content"]/div[3]/div/section[1]/div[1]/ul/li[1]/div/h3/a').click()
sleep(2)
site_dadosgov.find_element_by_xpath('//*[@id="dataset-resources"]/ul/li[1]/a').click()
sleep(2)
site_dadosgov.find_element_by_xpath('//*[@id="content"]/div[3]/section/div[1]/div[1]/ul/li/a').click()
sleep(10)

site_dadosgov.quit()

