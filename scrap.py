import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

badges_list = []
total_jobs = 0

for p in range(1, 153):

    URL = f'https://web3.career/defi-jobs?page={p}'
    print(URL)
    page = requests.get(URL)

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
print(total_jobs)

with open('badges.csv', 'w') as f:
    for key in dict_with_badges.keys():
        f.write("%s, %s\n" % (key, dict_with_badges[key]))


