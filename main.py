
import time
from bs4 import BeautifulSoup
import requests
import telepot

token = '5341234760:AAE9OvCDSSiuWY-itM8TQvKeEv4DpCownRA'

receiver_id = 862482751

bot = telepot.Bot(token)



page_no = 0

company_and_role = []
posted = []

while True:
    url = "https://www.linkedin.com/jobs/search/?currentJobId=3004243379&f_TPR=r86400&geoId=102713980&keywords=%22data%20analyst%22&location=India&position=12&pageNum=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_no+=1

    results = soup.find_all('div', {'class': 'base-search-card__info'})
    print(len(results))
    time.sleep(1)
    for i in results:
        time.sleep(1)
        try:
            if "minute" in i.find('time', {'class': 'job-search-card__listdate--new'}).text.strip():
                if i.find('h3', {'class': 'base-search-card__title'}).text.strip()+ str(" at ")  + i.find('h4', {'class': 'base-search-card__subtitle'}).text.strip() in company_and_role:
                    print("already exists")
                else:
                    company_and_role.append(i.find('h3', {'class': 'base-search-card__title'}).text.strip()+ str(" at ")  + i.find('h4', {'class': 'base-search-card__subtitle'}).text.strip())
                    bot.sendMessage(receiver_id, i.find('h3', {'class': 'base-search-card__title'}).text.strip()+ str(" at ")  + i.find('h4', {'class': 'base-search-card__subtitle'}).text.strip() + str("\n") + i.find('time', {'class': 'job-search-card__listdate--new'}).text.strip() )
                    print(i.find('h3', {'class': 'base-search-card__title'}).text.strip())
                    print(i.find('h4', {'class': 'base-search-card__subtitle'}).text.strip())
                    try:
                        print(i.find('time', {'class': 'job-search-card__listdate--new'}).text.strip())
                    except:
                        pass
        except:
            pass

    print(company_and_role)

    
    time.sleep(5)

