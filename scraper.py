from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

browser = webdriver.Chrome("C:\\Coding\\Python\\Class 128\\Class 128\\chromedriver.exe")
browser.get(START_URL)

time.sleep(10)
scrape_data = []
def scrape():
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    bright_star_table = soup.find('table',attrs = {'class','wikitabl'})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    for row in table_rows:
        table_cols = row.find_all('td')
        temp_list = []
        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)
        scrape_data.append(temp_list)
scrape()

stars_data = []
for i in range(0,len(scrape_data)):
    Star_names = scrape_data[i][1]
    Distance = scrape_data[i][3]
    Mass = scrape_data[i][5]
    Radius = scrape_data[i][6]
    Lum = scrape_data[i][7]
    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)
print(stars_data)
headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']
Star_name_df_1 = pd.DataFrame(stars_data, columns = headers)
Star_name_df_1.to_csv('scrape_data.csv', index = True, index_label = 'id')