import os
import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


class Stock_report():
    def __init__(self):
        self.url = 'https://www.investing.com/equities/'
        self.url_default = 'https://www.investing.com/etfs/'
        self.symbol = []
        self.symbol_default = ['powershares-qqqq', 'proshares-ultra-qqq-etf', 'spdr-s-p-500']
        self.prices_now = []
        self.prices_52w = []
        self.f_name = './stock_report.xlsx'

    def process(self):
        self.symbol_req()
        self.open_br()
        self.crawl_prices()
        self.update_file()

    def symbol_req(self):
        # symbol = input('Please tell me the ticker of the stock to crawl. : ').split()
        self.symbol = ['apple-computer-inc', 'google-inc', 'nvidia-corp', 'tesla-motors', 'coca-cola-co', 'pepsico', 'asml-holdings']

    def open_br(self):
        self.browser = webdriver.Chrome()

    def crawl_prices(self):
        browser = self.browser
        symbol = self.symbol
        symbol_default = self.symbol_default
        prices_now = self.prices_now
        prices_52w = self.prices_52w
        xp_now = '//*[@id="__next"]/div/div/div/div[2]/main/div/div[1]/div[2]/div[1]/span'
        xp_52w = '//*[@id="__next"]/div/div/div/div[2]/main/div/div[1]/div[2]/ul/li[3]/div[2]'
        for i in symbol:
            browser.get(self.url + i)
            price_now = browser.find_element(By.XPATH, xp_now).text
            prices_now.append(float(price_now))
            price_52w = browser.find_element(By.XPATH, xp_52w).text
            price_52w = price_52w[(price_52w.find('-') + 2):]
            prices_52w.append(float(price_52w))
        xp_now = '//*[@id="last_last"]'
        xp_52w = '//*[@id="leftColumn"]/div[9]/div[5]/span[2]'
        for i in symbol_default:
            browser.get(self.url_default + i)
            price_now = browser.find_element(By.XPATH, xp_now).text
            prices_now.append(float(price_now))
            price_52w = browser.find_element(By.XPATH, xp_52w).text
            price_52w = price_52w[(price_52w.find('-') + 2):]
            prices_52w.append(float(price_52w))
        browser.quit()

    def update_file(self):
        f_name = self.f_name
        prices_now = self.prices_now
        prices_52w = self.prices_52w
        wb = openpyxl.load_workbook(f_name)
        ws = wb.active
        for i,j in enumerate(prices_now):
            ws["E"+str(15 + i)].value = j
        for i,j in enumerate(prices_52w):
            ws["C"+str(3 + i)].value = j
        wb.save(f"stock_report_{str(datetime.today())[2:11]}.xlsx")


if __name__ == '__main__':
    sr = Stock_report()
    sr.process()