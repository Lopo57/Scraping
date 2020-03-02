import requests
import re
import urllib.request
from bs4 import BeautifulSoup

class Scraping():
    
    def __init__(self, url, keyword, page_url, output):
        self.url = url              #アクセス先URL
        self.keyword = keyword      #検索キーワード
        self.page_url = page_url    #ページ指定用URL
        self.output = output        #出力先ディレクトリ
        self.html = ""              #受け取ったhtml
        self.soup = ""              #BeautifulSoup

    #指定したページのソースを取得
    def GetHtmlSouce(self, page_num):

        #URL・キーワード・ページ指定でアクセス先を作成
        url = self.url + self.keyword + self.page_url + str(page_num)
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
        url = "https://pixabay.com/ja/"
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        print(response.getcode())
        #print(response.read())


    #------Seter------#
    #urlをセット
    def SetUrl(self, url):
        self.url = url

    #htmlをセット
    def SetHtml(self, html):
        self.html = html

    #soupをセット
    def SetSoup(self, soup):
        self.soup = soup

    #------Geter------#
    #urlをゲット
    def GetUrl():
        return self.url

    #htmlをゲット
    def GetHtml():
        return self.html

    #soupをゲット
    def GetSoup():
        return self.soup