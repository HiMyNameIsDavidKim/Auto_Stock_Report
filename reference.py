# 나도코딩의 주식정보 크롤링 강의를 reference로 만들었다.
# 네이버 금융 -> 국내증시 -> 시가총액, 여기서 필요한 정보만 체크해서 크롤링.
# 사용 라이브러리 : 판다스, 셀레늄 / 사용 프로그램 : 크롬 드라이버

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

items_to_select = ['영업이익', '자산총계', '매출액']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..')
    label = parent.find_element(By.TAG_NAME, 'label')
    if label.text in items_to_select:
        checkbox.click()

btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

last_page = '//*[@id="contentarea"]/div[3]/table[2]/tbody/tr/td[12]'
browser.find_element(By.XPATH, last_page).click()
last_page_url = browser.current_url
last_page_no = int(last_page_url[(last_page_url.find('=') + 1):])
print(last_page_no)

for idx in range(1,(last_page_no + 1)):
    browser.get(url + str(idx))
    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    f_name = './sise.csv'
    if os.path.exists(f_name):
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    else :
        df.to_csv(f_name, encoding='utf-8-sig', index=False)
    print(f'No.{idx} page is completed.')

browser.quit()