# Auto Stock Report
* Automatic nasdaq's stock reporting system.

## [Instructions]
* Way to crawl : Use Chrome Driver and selenium.
* Crawl from this site : www.investing.com
* Default stocks : AAPL, GOOGL, NVDA, TSLA, KO, PEP, ASML
* Default ETFs : QQQ, QLD, SPY

## [How to Run?]
* Open `stock_report.py` python file. Just run.
* Saved file is here. `report` directory.

## [Result]
* Everyday, update today's stock price.
    * You can check daily big moments.
* When 52 week highest price is changed, update 52W stock price.
    * You can check node that each low price. It can be your index to invest.
* Every monthly start day, update this month's starting stock price.
    * You can check today's price is how many diffrent from monthly starting stock price.

## [Notice]
* Don't decide to buy stock only check a relative price. Stock prices are determined by `Standard Interest Rates` and `consumer psychology`.
* Don't make too much traffic from the site.