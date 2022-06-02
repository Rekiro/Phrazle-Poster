import requests
from bs4 import BeautifulSoup

class Lexico:
  def __init__(self):
       
    self.url = 'https://www.lexico.com/definition/'

  def key_words_search_words(self, user_message):
    words = user_message.split()[1:]
    keywords = '_'.join(words) #i_love_you
    phrase = ' '.join(words) #i love you
    return keywords, phrase

  def search(self, keywords):
    response = requests.get(self.url+keywords)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    Meaning = soup.find(class_ = "ind one-click-content")
    Examples = soup.find_all("em")
    return Meaning, Examples
      
#  def send_link(self, result_links, search_words): 
#    send_link = set()
#    for link in result_links:
#        text = link.text.lower()
#        if search_words in text:  
#          send_link.add(link.get('href'))
#    return send_link