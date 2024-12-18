import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/Holyport_College', auth=('user', 'pass'))

print(r.text.split("\n")[543])
