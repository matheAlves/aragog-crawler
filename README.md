# aragog-crawler
Python web scraper for the wizardingworld.com website

# Features
Scraps content from each of J.K. Rowling original writings from https://www.wizardingworld.com/writing-by-jk-rowling
![example](./dicts.png)

# Usage
- Install Dependencies
`python3 -m pip install -r requirements.txt`

- Then simply call the extract_content() method from crawler.py and it should return a list of dictionaries containing the 'title' and 'text' for each of the writings (there are 93 as of november 2022)

You need to have Selenium browser driver for Chrome installed
(https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

# Reference
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
[Real Python](https://realpython.com/beautiful-soup-web-scraper-python/)  
[Selenium with Python](https://selenium-python.readthedocs.io/index.html)  
[Wizarding World Website](https://www.wizardingworld.com/)

I don't own any of the content scraped. This project is for educational purposes only.
