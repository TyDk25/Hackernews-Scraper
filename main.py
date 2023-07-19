import requests
from bs4 import BeautifulSoup
import pprint


def parser(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def multiple_pages(link1, link2):
    soup1 = parser(link1)
    soup2 = parser(link2)
    return soup1, soup2

page1_url = 'https://news.ycombinator.com/news'
page2_url = 'https://news.ycombinator.com/news?p=2'

soup1, soup2 = multiple_pages(page1_url,page2_url)

links_page1 = soup1.select('.titleline > a')
links_page2 = soup2.select('.titleline > a')

subtext = soup1.select('.subtext')
subtext2 = soup2.select('.subtext')

def sort_stories(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):

        title = item.getText()
        href = item.get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:

                hn.append({'title' : title, 'link': href, 'votes': points})
    return hn


hn_list1 = create_custom_hn(links_page1,subtext)
hn_list2 = create_custom_hn(links_page2,subtext2)

all_pages = hn_list1 + hn_list2

pprint.pprint(sort_stories(all_pages))


sorted_hn_list = sort_stories(all_pages)

sorted_hn_list = sort_stories(all_pages)


print(sorted_hn_list)
