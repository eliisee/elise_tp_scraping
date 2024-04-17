# create new session and open the connectionto get cookies
URL = 'https://www.scrapethissite.com/pages/simple/'
s = requests.Session()
r = s.get(URL)
r=s.post(url + suburl, params=payload, headers=headers)

# ectract information
soup = BeautifulSoup(r.text, 'https://www.scrapethissite.com/pages/simple/')

data = soup.find_all('table')[0]
df = pd.read_html(str(data))[0]