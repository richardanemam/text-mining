#@autor: Richard Anemam
#Date: Sep 3, 2018
#Scraping text with BeatifulSoup

import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup

class TextMining:

    def __init__(self, quote_page):
        self.quote_page = quote_page

    def getHtml(self):
        pageHtml = requests.get(self.quote_page)
        return pageHtml

    def getStatus(self):
        pageStatus = self.getHtml()
        return pageStatus.status_code
    
    def parsingIntoBs(self):
        page = self.getHtml()
        soup = BeautifulSoup(page.content, "html.parser")
        return soup        

    def getData(self):
        soup = self.parsingIntoBs()
        name = soup.find('div', attrs={"class": "col-sm-10 forecast-text"}).get_text()
        return name

    def exportToCsv(self):
        with open("data.csv", "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([self.getData(), datetime.now()])

    def exportToTxt(self):
        writer = open("data.txt", "w")
        writer.write(self.getData())
        writer.close()

def main():
    text = TextMining("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.W43pfugzpEY")
    print(text.getStatus(), '\n')
    print(text.getData())
    text.exportToCsv()
    text.exportToTxt()

if __name__ == "__main__":
   main()