import requests
from bs4 import BeautifulSoup

URL = 'https://web3.career/defi-jobs'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

jobs = soup.findAll("tr", {"class": "table_row"})

print(jobs)

for job in jobs:
    print(job.find('h2', {'class': 'my-primary'}).text)
    badges = job.findAll('a', {'class': 'text-shadow-1px'})
    for badge in badges:
        print(badge.text)