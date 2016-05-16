
# coding: utf-8

# In[1]:

import requests
import urllib
import bs4


# In[12]:

raw_question = input("Your Question for Stackoverflow:")
domain = "https://stackoverflow.com"
question=urllib.parse.quote_plus(raw_question + " is:answer score:10")
response = requests.get(domain + "/search?q="+question)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, "lxml")
answers = soup.select("div.summary > div.result-link")
if len(answers) > 0:
    link = answers[0].find('a')['href']
    response = requests.get(domain + link)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "lxml")
    answer = soup.select("div.accepted-answer .post-text")
    print(answer[0].getText())
else:
    print("No result found :(")
input("Quit...")


# In[ ]:



