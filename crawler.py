import requests
from parsel import Selector
from bs4 import BeautifulSoup


def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    return response

# it is necessary to find a way to scroll the page for all the url to be scraped
def extract_urls(content):
    selector = Selector(content.text)
    return selector.css("div.Hub_root__qduRu a::attr(href)").getall()

def browse_pages(urls):
    BASE_URL = 'https://www.wizardingworld.com'
    next_page = urls[0]

    try:
        for index, url in enumerate(urls, start=1):
            content = fetch_content(BASE_URL + next_page)
            soup = BeautifulSoup(content.content, 'html.parser')
            title = soup.find(class_="ArticleHero_title__cOam6").text
            print(title)
            next_page = urls[index]
    except IndexError:
        print("end of list")

def init():
    INITIAL_URL = 'https://www.wizardingworld.com/writing-by-jk-rowling'
    content = fetch_content(INITIAL_URL)
    urls = extract_urls(content)
    browse_pages(urls)