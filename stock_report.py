import os
import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


class Stock_report():
    def __init__(self):
        self.url = 'https://seekingalpha.com/symbol/'
        self.symbol = []
        self.symbol_default = ['qqq', 'qld', 'spy']
        self.prices_now = []
        self.f_name = './stock_report.xlsx'

    def process(self):
        self.symbol_req()
        self.open_br()
        self.crawl_prices()
        self.update_file()

    def symbol_req(self):
        # symbol = input('Please tell me the ticker of the stock to crawl. : ').split()
        self.symbol = ['aapl', 'googl', 'nvda', 'tsla', 'ko', 'pep', 'asml']

    def open_br(self):
        self.browser = webdriver.Chrome()

    def crawl_prices(self):
        browser = self.browser
        symbol = self.symbol
        symbol_default = self.symbol_default
        prices_now = self.prices_now
        xp_now = '//*[@id="content"]/div/div[2]/div/div/div[1]/div/div[2]/span[1]'
        for i in symbol:
            browser.get(self.url + i)
            price_now = browser.find_element(By.XPATH, xp_now).text
            prices_now.append(float(price_now[1:]))
        for i in symbol_default:
            browser.get(self.url + i)
            price_now = browser.find_element(By.XPATH, xp_now).text
            prices_now.append(float(price_now[1:]))
        browser.quit()
    
    def update_file(self):
        f_name = self.f_name
        prices_now = self.prices_now
        wb = openpyxl.load_workbook(f_name)
        ws = wb.active
        for i,j in enumerate(prices_now):
            ws["E"+str(12 + i)].value = j
        wb.save(f"stock_report_{str(datetime.today())[2:11]}.xlsx")


if __name__ == '__main__':
    sr = Stock_report()
    sr.process()