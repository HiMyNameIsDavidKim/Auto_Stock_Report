import os
import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

f_name = './stock_report.xlsx'
wb = openpyxl.load_workbook(f_name)
ws = wb.active
ws["E"+str(12)].value = 123.00
wb.save(f"stock_report_{str(datetime.today())[2:11]}.xlsx")