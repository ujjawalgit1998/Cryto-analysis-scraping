import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import lxml



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.coindesk.com/coindesk20/"

driver.get(url)
html_data = driver.page_source

data = pd.read_html(html_data)[0]
filename = "crpto_data_coindesk.csv"
data.to_csv(filename)

driver.quit()
