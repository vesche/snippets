# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urlparse import urlsplit
from collections import deque
import re


def crawl(url):
    new_urls        = deque(["http://{}".format(url)])
    processed_urls  = set()
    emails          = []

    while len(new_urls):
        url = new_urls.popleft()
        processed_urls.add(url)

        parts       = urlsplit(url)
        base_url    = "{0.scheme}://{0.netloc}".format(parts)
        path        = url[:url.rfind('/') + 1] if '/' in parts.path else url

        print "Processing {}".format(url)
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, \
        requests.exceptions.ConnectionError):
            continue

        new_emails = re.findall(r"\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+", \
        response.text, re.I)
        for addr in new_emails:
            emails.append(addr)

        soup = BeautifulSoup(response.text)

        for anchor in soup.find_all('a'):
            link = anchor.attrs["href"] if "href" in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith("http"):
                link = path + link
            if not link in new_urls and not link in processed_urls:
                new_urls.append(link)

    with open("emails.txt", 'w') as f:
        f.write('\n'.join(emails))
