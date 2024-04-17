from bs4 import BeautifulSoup
import requests 

# create new session and open the connectionto get cookies
URL = 'https://www.scrapethissite.com/pages/simple/'
s = requests.Session()
r = s.get(URL)
#r=s.post(url + suburl, params=payload, headers=headers)

# ectract information
soup = BeautifulSoup(r.text, 'html.parser')

country_tags = soup.find_all('h3', class_='country-name')
capital_tags = soup.find_all('span', class_='country-capital')

for country, capital in zip(country_tags, capital_tags): 
    print(country.text, '-', capital.text)