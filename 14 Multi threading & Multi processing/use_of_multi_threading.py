'''
real world example:- multi threading for i/o bound task
Scenario: web Scraping

'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.geeksforgeeks.org/python-programming-language-tutorial/",
    "https://www.geeksforgeeks.org/ai-ml-and-data-science-tutorial-learn-ai-ml-and-data-science/",
    "https://www.geeksforgeeks.org/web-technology/"

]

def fetch_data(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,"html.parser")
    print(f"fetched{len(soup.text)} characters from {url}")


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_data,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()