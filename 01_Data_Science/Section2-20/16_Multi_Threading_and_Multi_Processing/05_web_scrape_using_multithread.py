'''
Real-world example: Multithreading for I/O bound tasks
Web scraping: this involves making numerous network requests to fetch web pages.
These are I/O bound because they spend a lot of time waiting for responses from servers.
Multithreading can siginificantly improve the performance by allowing multiple web pages to be fetched concurrently.
'''

import threading
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

urls = [
    'https://docs.langchain.com/oss/python/langchain/overview',
    'https://docs.langchain.com/langsmith/python/managed-deep-agents-overview',
    'https://docs.langchain.com/oss/python/langgraph/overview'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return (f'Fetched {len(soup.text)} characters from {url}')

# using thread library

# threads = []

# for url in urls:
#     thread = threading.Thread(target=fetch_content, args=(url, ))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print('All web pages fetched')

# Using threadpool

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(fetch_content, urls)

for result in results:
    print(result)

print('All web pages fetched')
