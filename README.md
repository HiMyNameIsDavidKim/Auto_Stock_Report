# Auto Stock Report
* Automatic nasdaq's stock reporting system.

## [Instructions]
* Way to crawl : Use Chrome Driver and selenium.
* Crawl from this site : www.investing.com, www.google.com, www.finance.yahoo.com, www.bls.gov
* Default stocks : AAPL, KO, NVDA, TSLA, GOOGL, PEP, ASML
* Default ETFs : QQQ, SPY
* Version
  * v1.0 : basic version.
  * v2.0 : change site to google and yahoo finance. all method's speed is improved.
  * v2.1 : when find now price and 52w price, use list comprehension. when find monthly price, use text finding.
  * v2.2 : monthly update is too slow -> solution : origin file update only 1 time. separate month checker method.
  * v2.3 : Daily alarm, node alarm, FED alarm, CPI alarm is updated. language update to ENG.

## [How to Run?]
* Open `latest_version` and open py file.
* Do `environment setting`.
* run file.
* Saved report is here. `report` directory.

## [Environment]
* [`install chromedriver`](https://chromedriver.chromium.org/downloads)
* pip install selenium
* pip install bs4
* pip install openpyxl
* pip install pandas
* pip install datetime

## [Explain of Result]
* Every day, update today's stock price.
    * You can check daily big moments.
* When 52 week the highest price is changed, update 52W stock price.
    * You can check node that each low price. It can be your index to invest.
* Every monthly start day, update this month's starting stock price.
    * You can check today's price is how many diffrent from monthly starting stock price.

## [Notice]
* Don't decide to buy stock only check a relative price.
* Stock prices are determined by `Standard Interest Rates` and `consumer psychology`.
* Don't make too much traffic from the site.



