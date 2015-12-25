#!/usr/bin/env python

import re
import requests
import subprocess
import sys
from bs4 import BeautifulSoup

token_pattern = re.compile(r'var token_key="(.*?)";')
usage_text = './mtt.py <movie title>'

if __name__ == "__main__":
    try:
        title = ' '.join(sys.argv[1:])
    except:
        print usage_text
        sys.exit(0)

    with requests.Session() as session:
        session.headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; \
        Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0"}

        # extract token
        response = session.get("http://movietv.to/")
        soup = BeautifulSoup(response.content, "html.parser")

        script = soup.find("script", text=token_pattern).get_text()
        match = token_pattern.search(script)
        if not match:
            raise ValueError("Cannot find token!")

        token = match.group(1)

        # search for the movies
        response = session.post("http://movietv.to/index/loadmovies", data={
            "loadmovies": "showData",
            "page": "1",
            "abc": "All",
            "genres": "",
            "sortby": "Popularity",
            "quality": "All",
            "type": "movie",
            "q": title,
            "token": token
        })

        soup = BeautifulSoup(response.content, "html.parser")

        movie_links = []
        for link in soup.find_all('a'):
            movie_links.append(link.get('href'))

        for i in range(len(movie_links)):
            movie_name = movie_links[i]
            print '{0}. {1}'.format(i+1, ' '.join(movie_name.split('-')[1:]))

        movie_numb = input("Which movie (#)? ")

        response = session.get("http://movietv.to/{}".format(movie_links[movie_numb-1]))
        soup = BeautifulSoup(response.content, "html.parser")

        for link in soup.find_all('source'):
            movie_link = link.get('src')

        c_link = '&'.join(movie_link.split('&')[:2])

        subprocess.Popen(['vlc', c_link])
