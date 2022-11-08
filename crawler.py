from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from bs4 import BeautifulSoup

INITIAL_URL = "https://www.wizardingworld.com/writing-by-jk-rowling"
browser = webdriver.Chrome()


def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as err:
        print(err.args)
    return response


def extract_urls():
    urls = [
        url.get_attribute("href")
        for url in browser.find_element(By.CLASS_NAME, "Hub_root__qduRu").find_elements(
            By.CSS_SELECTOR, "a"
        )
    ]
    return urls


def scroll():
    browser.get("https://www.wizardingworld.com/writing-by-jk-rowling")


    print(len(urls))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    urls = extract_urls()
    print(len(urls))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    urls = extract_urls()
    print(len(urls))

    # urls = selector.css("div.Hub_root__qduRu a::attr(href)").getall()
    # urls.pop(0)
    # return urls


# current_urls = extract_urls(fetch_content(INITIAL_URL))

# while True:
#     def scroll_page():

#         browser.get("https://www.wizardingworld.com/writing-by-jk-rowling")
#         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# it is necessary to find a way to scroll the page for all the url to be scraped


def extract_content(urls):
    result = []
    BASE_URL = "https://www.wizardingworld.com"
    try:
        for url in urls:
            first_word = ""
            content = fetch_content(BASE_URL + url)
            soup = BeautifulSoup(content.content, "html.parser")
            title = soup.find(class_="ArticleHero_title__cOam6").text
            content = soup.find(class_="ArticleNewsFeature_articleBody__1chXE")
            extract = [span.extract().text for span in content.find_all("span")]
            if extract:
                first_word = extract[1]
                text = first_word + " " + content.get_text(strip=True)
            else:
                text = content.get_text(strip=True)
            result.append({"title": title, "text": text})
    except Exception as err:
        print(err.args)
    return result
