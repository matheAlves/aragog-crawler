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
    urls = selector.css("div.Hub_root__qduRu a::attr(href)").getall()
    urls.pop(0)
    return urls


def extract_content(urls):
    result = []
    BASE_URL = "https://www.wizardingworld.com"

    try:
        for url in urls:
            first_word = ''
            content = fetch_content(BASE_URL + url)
            soup = BeautifulSoup(content.content, "html.parser")
            title = soup.find(class_="ArticleHero_title__cOam6").text
            content = soup.find(class_="ArticleNewsFeature_articleBody__1chXE")
            extract = [span.extract().text for span in content.find_all("span")]
            if extract:
                first_word = extract[1]
                text = first_word + ' ' + content.get_text(strip=True)
            else:
                text = content.get_text(strip=True)
            result.append({"title": title, "text": text})
    except Exception as err:
        print(err.args)
    return result

def crawl():
    INITIAL_URL = "https://www.wizardingworld.com/writing-by-jk-rowling"
    content = fetch_content(INITIAL_URL)
    urls = extract_urls(content)
    return extract_content(urls)

    
