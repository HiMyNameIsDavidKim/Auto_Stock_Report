# Auto Stock Report
* Automatic nasdaq's stock reporting system.

## [Instructions]
* way to crawl : Use Chrome Driver and selenium.
* crawl from this site : www.investing.com
* default stocks : AAPL, GOOGL, NVDA, TSLA, KO, PEP, ASML
* default ETFs : QQQ, QLD, SPY

## [How to Run?]
* Open `stock_report.py` python file. Just run.
* Saved file is here. `report` directory.

## [Result]
* Everyday, update today's stock price.
    * You can check daily big moments.
* When 52 week highest price is changed, update 52W stock price.
    * You can check node that each low price. It can be your index to invest.
* Every month start day, update this month's starting stock price.
    * You can check today's price is how many diffrent from this month start day's price.

## [Notice]
* Stock prices are determined by `Standard Interest Rates` and `consumer psychology`. Don't decide to buy stock only check a relative price.
* Don't make too much traffic from the site.