# create new session and open the connectionto get cookies
URL = 'google.com'
s = requests.Session()
r = s.get(URL)
r=s.post(url + suburl, params=payload, headers=headers)