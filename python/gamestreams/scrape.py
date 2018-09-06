# -*- coding: utf-8 -*-

import bs4
import requests

URL = 'https://old.reddit.com'
subreddits = { 'nba': '/r/nbastreams' }

session = requests.session()
headers = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i386; rv:39.0) Gecko/20100101 Firefox/39.0' }
session = requests.Session()
session.headers.update(headers)

def make_soup(url):
    r = session.get(url)
    page = r.content
    soup = bs4.BeautifulSoup(page, 'html.parser')
    return soup

def get_threads():
    soup = make_soup('{}{}'.format(URL, subreddits['nba']))

    threads = []
    for tag in soup.find_all('a', 'title may-blank '):
        thread_uri = tag.get('href')
        t = thread_uri.lower()
        if 'game_thread' in t or 'channel_thread' in t:
            threads.append('{}{}'.format(URL, thread_uri))
    return threads

def get_links(thread):
    soup = make_soup(thread)

    links = []
    for div in soup.findAll('div', {'data-author': 'nbasticky'}):
        for a in div.findAll('a'):
            try:
                link = a['href']
            except KeyError:
                continue
            if 'reddit.com' not in link and link.startswith('http'):
                links.append(link)

def get_streams(link):
    soup = make_soup(link)

    # try m3u8 first
    find_m3u8(soup)

    find_iframe(soup)

#def find_m3u8(soup):
#    for 

def find_iframe(soup):
    for iframe in soup.find_all('iframe'):
        print(iframe['src'])

#
# print(get_threads())
# for thread in get_threads():
#     links = get_links(thread)
#     for link in links:
#         get_streams(link)
#

get_links("https://old.reddit.com/r/nbastreams/comments/8mukr5/game_thread_golden_state_warriors_houston_rockets/")

get_streams('http://streams.trendingsports.club/2018/01/nba-tv-247-live-stream.html')














