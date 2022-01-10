from core import WebAbstract, WebFactory, MyWebs
import requests
import urllib.parse
from bs4 import BeautifulSoup

class PelisEnHd(WebAbstract):

    def __init__(self):
        self.title = "pelisenhd"
        self.url = "https://www.pelisenhd.net"
        self.type = "tvshow"

    def getlink_from_keyword(self, keyword):
        r = requests.get(f"{self.url}?s={urllib.parse.quote_plus(keyword)}")
        soup = BeautifulSoup(r.text, 'lxml')
        val = soup.find(class_='card__cover')
        if val:
            return val.find('a')['href']
        return None


    def scan(self, shows_list):
        for record in shows_list:
            if record.type != self.type:
                continue
            for keyword in record.search_data.get('keywords'):
                link = self.getlink_from_keyword(keyword)
            return {}


web_factory = WebFactory()
web_factory.register_web('pelisenhd', PelisEnHd())
my_webs = MyWebs()
my_webs.add_website(web_factory.get_web('pelisenhd'))