import requests
from bs4 import BeautifulSoup

def get_text_if_exists(html_element):
    if html_element != None: 
        return html_element.get_text()
    else: 
        return ''

def get_serial_no(html_element):
    if html_element != None: 
        return html_element.get_text() + '. '
    else:
        return ''

def get_sense_region(html_element):
    if html_element != None: 
        return '***' + html_element.get_text(strip = True) + '*** '
    else :
        return ''

def get_sense_register(html_element):
    if html_element != None: 
        return '***<' + html_element.get_text('*', strip = True) +'>*** '
    else: 
        return ''

def get_grammatical_note(html_element):
    if html_element != None: 
        return '***[' + html_element.get_text() + ']***'
    else: 
        return ''

def get_form_groups(html_element):
    if html_element != None: 
        return '**(' + html_element.get_text(strip = True) + ')**'
    else: 
        return ''

      

class Dictionary:
  def __init__(self):
       
    self.url = 'https://www.lexico.com/definition/'
    self.search_url = 'https://www.lexico.com/search?utf8=✓&filter=en_dictionary&dictionary=en&query='

  def define(self, user_message):
    
    splitted_words = user_message.split()[1:]
    keywords = '_'.join(splitted_words) #i_love_you
    the_word_or_phrase = ' '.join(splitted_words).title() #I Love You

    response = requests.get(self.url + keywords, allow_redirects = True)

    if response.status_code != 406:
    
      content = response.content
      soup = BeautifulSoup(content, 'html.parser')
  
      phonetic_spelling = soup.find('span', class_ = 'phoneticspelling')
      sections = soup.findAll('section', class_ = 'gramb')
  
      definition = ''.join(['**', the_word_or_phrase, '**\n', get_text_if_exists(phonetic_spelling), '\n\n'])
  
      for sec in sections: 
        #sec.prettify()
     
        word_type = sec.find('span', class_ = 'pos')
    
        sense_registers = sec.find('span', class_ = 'sense-registers')
        sense_regions = sec.find('span', class_ = 'sense-regions')
    
        list = sec.find_all('li', class_ = None)
  
        definition = ''.join([definition, '**__', word_type.get_text().title(), '__**\n'])
        if len(list) == 1:
          definition = ''.join([definition, get_sense_region(sense_regions),  get_sense_register(sense_registers), '\n'])
  
        for entries in list: 
          
          p = entries.find('p')
          serial_no = p.find('span', class_ = 'iteration')
          sense_regions = p.find('span', class_ = 'sense-regions')
          sense_registers = p.find('span', class_= 'sense-registers')
          grammatical_note = p.find('span', class_ = 'grammatical_note')
          form_groups = p.find('span', class_ = 'form-groups')
          meaning =p.find('span', class_ ='ind one-click-content')
          example = entries.find('em')
          if meaning == None: 
              meaning = sec.find('div', class_='crossReference')
  
          definition = ''.join([definition, get_serial_no(serial_no), get_sense_region(sense_regions), get_sense_register(sense_registers), get_grammatical_note(grammatical_note), get_form_groups(form_groups), ' ', meaning.get_text(), '\n   *', get_text_if_exists(example), '*\n\n' ])

    
      return definition, self.url + keywords
      
    else: 
      
      # query = '+'.join(splitted_words) #i+love+you
      # #the_word_or_phrase = ' '.join(splitted_words).title() #I Love You

      # response = requests.get(self.search_url + query, allow_redirects = True)
      # content = response.content
      # soup = BeautifulSoup(content, 'html.parser')

      # search_heading = soup.find('h2', class_ = 'searchHeading')
      
      return None, None


    
#  def send_link(self, result_links, search_words): 
#    send_link = set()
#    for link in result_links:
#        text = link.text.lower()
#        if search_words in text:  
#          send_link.add(link.get('href'))
#    return send_link


