from bs4 import BeautifulSoup
import requests
from collections import deque

class PageData:

    def __init__(self, link, title):
        self.link = link
        self.title = title

class Decorator:
    pass

# [1..10]
class Crawler:

    def __init__(self, depth):
        self.Pages = []
        self.depth = depth-1
        self.links = []
        self.vis = set()

    def requestData(self, url):
        try:
            raw_data = requests.get(url)
            raw_data.raise_for_status()
            # print(raw_data.text)
            return raw_data.text
        except Exception as e:
            print(e)

    def getTitleFromUrl(self, url):
        html_data = self.requestData(url)
        # print(html_data)
        soup = BeautifulSoup(html_data, 'html.parser')
        return soup.title.string

    def crawl(self, html_data):
        soup = BeautifulSoup(html_data, 'html.parser')
        title = soup.title.string
        for link in soup.find_all('a'):
            if self.filterUrl(link.get('href')):
                url = link.get('href')
                # self.vis.add(url)
                self.links.append((url, title))
        return title

    def filterUrl(self, url):
        if url and "https" in url and url not in self.vis:
            return True
        return False

    def handler(self, url):
        i = 0
        # htmldata = self.requestData(url)
        # title = self.getTitleFromUrl(url)
        self.links.append((url, ""))
        while(self.depth != 0):
            if i < len(self.links):
                cur_link, _ = self.links[i]
                if cur_link in self.vis:
                    i+=1
                    continue
                self.vis.add(cur_link)
                html_data = self

                # print(html_data)
                if html_data:
                    cur_title = self.crawl(html_data)
                    pageData = PageData(cur_link, cur_title)
                    print(pageData.link, pageData.title)
                    self.Pages.append(pageData)
            else:
                break
            self.depth -= 1
            i+=1



if __name__ == '__main__':
    crawler = Crawler(10)
    # print(crawler.links)
    crawler.handler("https://en.wikipedia.org/wiki/Google")
    # print(crawler.vis)






#
# class Request:
#
#     def __init__(self):
#         pass
#
#     def getData(self, url):
#
#         try:
#             raw_data = requests.get(url)
#             raw_data.raise_for_status()
#             return raw_data
#         except Exception as e:
#             print(e)
