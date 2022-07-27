import requests
from bs4 import BeautifulSoup
# from datetime import datetime
# from apscheduler.scheduler import Scheduler
# import schedule
# import time


class Phrazle_Answer: 

  def __init__(self):
    self.url = 'https://uppolice.org/phrazle-answer/'
    self.headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}

  def one_time(self):

    response = requests.get (self.url, headers = self.headers, allow_redirects=True)
    
    if response.status_code >= 400: 
      return "Bad Request. Status Code: " + response.status_code
    
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    details = soup.findAll('td', attrs={'style': 'width: 50%; height: 24px;'})
    date = soup.find('td', attrs = {'style': 'width: 218.582px;'})
    answer = soup.find('td', attrs = {'style': 'width: 422.059px;'})

    result = ''
    result = ''.join([result, 'Date: ', date.get_text(), '\n**Today\'s Phrazle answer:** ||', answer.get_text().upper(), '||\n**Meaning:** ||*', details[7].get_text(), '*||'])

    return result

  def daily_answers(self):

    # url = 'https://uppolice.org/phrazle-answer/'
    # headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}

    response = requests.get (self.url, headers = self.headers, allow_redirects=True)
  
    if response.status_code >= 400: 
      return "Bad Request. Status Code: " + response.status_code
    
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    details = soup.findAll('td', attrs={'style': 'width: 50%; height: 24px;'})
    date = soup.find('td', attrs = {'style': 'width: 218.582px;'})
    answer = soup.find('td', attrs = {'style': 'width: 422.059px;'})

    result = ''

    for i in range(0, 6, 2):
      result = ''.join([result, details[i].get_text().capitalize(), ': ', details[i+1].get_text().capitalize(), '\n'])

    result = ''.join([result, '**Today\'s Phrazle answer:** ', answer.get_text().upper(), '\n**Meaning:** *', details[7].get_text(), '*\nDate: ', date.get_text(), '\nPhrazle web official website: >https://solitaired.com/phrazle<' ])

    return result
      


    # schedule.every().minute.at(":05").do(answer)
    # while True:
    #   schedule.run_pending()
    #   time.sleep(1)

    

    # #Create a scheduler and start it
    # sched = Scheduler()
    # sched.start()

    # exec_time = time(16, 45, 0)

    # # Store the job in a variable in case we want to cancel it
    # job = sched.add_time_job(answer, exec_time, ['my_text'])
    # return job



      
    #  # This function runs periodically every 1 second
    # t = threading.Timer(1, answer)
    # t.start()

    # now = datetime.now()

    # current_time = now.strftime("%H:%M:%S")
    # #print("Current Time =", current_time)

    # if(current_time == '16:14:00'):  # check if matches with the desired time
    #   return answer()

      
        
    
        

    
    

    
    