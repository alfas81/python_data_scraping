from lxml import html
import requests

page = requests.get('https://www.flashscore.com/football/england/premier-league-2018-2019/results/')
tree = html.fromstring(page.content)

out = tree.xpath("//div[@class='sportName soccer']//@id")
print(out)