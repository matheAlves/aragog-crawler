from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from bs4 import BeautifulSoup

def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as err:
        print(err.args)
    return response

def extract_urls(browser):
    urls = [
        url.get_attribute("href")
        for url in browser.find_element(By.CLASS_NAME, "Hub_root__qduRu").find_elements(
            By.CSS_SELECTOR, "a"
        )
    ]
    return urls

def scroll_page():
    browser = webdriver.Chrome()
    browser.get("https://www.wizardingworld.com/writing-by-jk-rowling")
    curr_urls = extract_urls(browser)
    print("fetching urls...")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        next_urls = extract_urls(browser)
        if len(next_urls) > len(curr_urls):
            curr_urls = next_urls
            pass
        elif len(next_urls) == len(curr_urls):
            break
    curr_urls.pop(0)
    return curr_urls

def extract_content():
    urls = scroll_page()
    print("fetching content...")
    result = []
    try:
        for url in urls:
            first_word = ""
            content = fetch_content(url)
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
