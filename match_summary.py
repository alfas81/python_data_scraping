import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html 

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  

  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

url = 'https://www.flashscore.com/football/england/premier-league-2018-2019/results/'  

def get_match_links(url):
	r = Render(url)  
	result = r.frame.toHtml()
	content = html.fromstring(str(result))
	raw_links = content.xpath("//div[@class='sportName soccer']//@id")
	full_links = ["https://www.flashscore.com/match/" + ids + "/#match-summary" for ids in raw_links]
	return(full_links)

get_match_links(url)