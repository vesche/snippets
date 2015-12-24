#!/usr/bin/env python

import sys
from mechanize import Browser

url = 'http://movietv.to'
uas = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'

if __name__ == "__main__":
    try:
        title = ' '.join(sys.argv[1:])
    except:
        print "./mtt.py <movie title>"
        sys.exit(0)

    br = Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', uas)]
    br.open(url)

    # search
    br.select_form(nr=0)
    br.form.set_value(title, nr=0)
    resp = br.submit()

    # write results to file
    with open('results.html', 'w') as f:
        f.write(resp.read())
