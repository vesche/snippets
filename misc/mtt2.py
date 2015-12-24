#!/usr/bin/env python

import re
import requests
import sys
from bs4 import BeautifulSoup

token_pattern = re.compile(r'var token_key="(.*?)";')

if __name__ == "__main__":
    try:
        title = ' '.join(sys.argv[1:])
    except:
        print "./mtt.py <movie title>"
        sys.exit(0)

    with requests.Session() as session:
        session.headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0"}

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

        for movie in soup.select("div.item"):
            title = movie.find("h2", class_="movie-title")

            print title.get_text()
