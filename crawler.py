import requests
from parsel import Selector
from bs4 import BeautifulSoup

result = []


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
    urls = selector.css("div.Hub_root__qduRu a::attr(href)").getall()
    urls.pop(0)
    return urls


def browse_pages(urls):
    BASE_URL = "https://www.wizardingworld.com"

    try:
        for url in urls:
            content = fetch_content(BASE_URL + url)
            soup = BeautifulSoup(content.content, "html.parser")
            title = soup.find(class_="ArticleHero_title__cOam6").text
            texts = soup.find(class_="ArticleNewsFeature_articleBody__1chXE")
            for span in texts.find_all("span"):
                span.decompose()
            result.append({"title": title, "text": texts.get_text(strip=True)})
    except Exception as err:
        print(err.args)


if __name__ == "__main__":
    INITIAL_URL = "https://www.wizardingworld.com/writing-by-jk-rowling"
    content = fetch_content(INITIAL_URL)
    urls = extract_urls(content)
