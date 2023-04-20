from selenium import webdriver
from bs4 import BeautifulSoup

import time
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars" 

browser=webdriver.Chrome("C:/Users/Owner/OneDrive/Desktop/whitehat/c127/to/chromedriver")
browser.get(START_URL)
time.sleep(10)



def scrape():
    headers = ["V Mag. (mV)",	"Proper name",	"Bayer designation",	"Distance (ly)", "Spectral class",	"Mass (M☉)",	"Radius (R☉)",	"Luminosity (L☉)"]
    planet_data = []
    for i in range(0, 214):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()





















