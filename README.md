# aragog-crawler
Python web scraper for the wizardingworld.com website (in development)

# Features
Returns a list of dictionaries containing the title and content of each of J.K. Rowling original writings from https://www.wizardingworld.com/writing-by-jk-rowling
![example](./dicts.png)

# Usage
Simply call the crawl() method from crawler.py and it will return the desired result (a list of dictionaries).

# Known Problems
When the https://www.wizardingworld.com/writing-by-jk-rowling/ page is first rendered it doesn't load all of the necessary urls, but does so as the page is scrolled down.
I am studying a way to automate that behavior.


# Reference
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
[Real Python](https://realpython.com/beautiful-soup-web-scraper-python/)
[Wizarding World Website](https://www.wizardingworld.com/)