import requests
from parsel import Selector
from bs4 import BeautifulSoup

def fetch_content() -> str:
    try:
        response = requests.get("https://www.wizardingworld.com/writing-by-jk-rowling")
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    return BeautifulSoup(response.content, 'html.parser').prettify()

def extract_urls(content: str) -> list[str]:
    selector = Selector(content)
    return selector.css("div.Hub_root__qduRu a::attr(href)").getall()