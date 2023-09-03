import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

badges_list = []

total_jobs = 31765
jobs_per_page = 35
pages = total_jobs//jobs_per_page

for p in range(1, pages+1):

    #URL = f'https://web3.career/defi-jobs?page={p}'
    URL = f'https://web3.career/?page={p}'
    page = requests.get(URL)
    print(f'{URL} - {page}')

    soup = BeautifulSoup(page.content, "html.parser")
    jobs = soup.findAll("tr", {"class": "table_row"})


    for job in jobs:
        #print(job.find('h2', {'class': 'my-primary'}).text)
        badges = job.findAll('a', {'class': 'text-shadow-1px'})
        total_jobs += 1
        for badge in badges:
            #print(badge.text.strip())
            badges_list.append(badge.text.strip())

def countOccurrence(a):
    k = {}
    for j in a:
        if j in k:
            k[j] +=1
        else:
            k[j] =1
    return k

dict_with_badges = countOccurrence(badges_list)
#print(countOccurrence(badges_list))
#print(pd.DataFrame([countOccurrence(badges_list)], index=1))

print(pd.DataFrame.from_dict(dict_with_badges, orient='index', columns=['times']).sort_values('times').tail(50))

with open('badges.csv', 'w') as f:
    for key in dict_with_badges.keys():
        f.write("%s, %s\n" % (key, dict_with_badges[key]))


