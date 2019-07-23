# python_data_scraping
Data scraping pipeline

import requests
import pandas as pd
import lxml
from lxml import html
import re
myurl = 'https://www.flashscore.com/football/england/premier-league-2018-2019/results/'
page_cont=requests.get(myurl)
tree = html.fromstring(page_cont.content)
url.parts = tree.xpath('//div[starts-with(@id,"g_1")]')
