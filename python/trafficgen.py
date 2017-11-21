#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Traffic generation script for Cyber Magic 2016
# https://github.com/vesche
#

import random
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


wiki_links = [
    "http://harrypotter.wikia.com/wiki/Special:Random",
    "http://occult.wikia.com/wiki/Special:Random",
    "http://paranormal.wikia.com/wiki/Special:Random" ]

amazon_links = [
    "https://amzn.com/B01FQ9Z8KG",
    "https://amzn.com/B00SFILQR0",
    "https://amzn.com/B00JZUJLBK",
    "https://amzn.com/B0024UM3DG",
    "https://amzn.com/B00647W9K2",
    "https://amzn.com/B0026PW67W",
    "https://amzn.com/076245945X",
    "https://amzn.com/1338097679",
    "https://amzn.com/B002YXBEKG",
    "https://amzn.com/B000FCUS14",
    "https://amzn.com/B0006IIV16",
    "https://amzn.com/B000H43358",
    "https://amzn.com/B000U0CP44",
    "https://amzn.com/B002IF67H0",
    "https://amzn.com/B003O68Q0S",
    "https://amzn.com/B001SBZ582",
    "https://amzn.com/B00Z82L68A",
    "https://amzn.com/B000ROHTBW",
    "https://amzn.com/B001K3BWTO",
    "https://amzn.com/B000H0DIE8",
    "https://amzn.com/B003BW790I" ]

search_links = [
    "https://www.google.com/search?q=how+to+perform+the+killing+curse",
    "https://www.google.com/search?q=why+do+robes+make+my+butt+look+big",
    "https://www.google.com/search?q=where+is+the+room+of+requirement",
    "https://www.google.com/search?q=how+to+make+felix+felicis",
    "https://www.google.com/search?q=why+is+hogwarts+internet+so+slow",
    "https://www.google.com/search?q=did+muggles+invent+the+internet",
    "https://www.google.com/search?q=how+do+i+get+rid+of+malware",
    "https://www.google.com/search?q=hungarian+horntail",
    "https://www.google.com/search?q=daniel+radcliffe+nudes",
    "https://www.google.com/search?q=how+to+make+a+flying+ford+anglia",
    "https://www.google.com/search?q=how+much+is+a+nimbus+2000",
    "https://www.google.com/search?q=best+hogsmeade+shops",
    "https://www.google.com/search?q=do+asian+girls+like+guys+with+scars",
    "https://www.google.com/search?q=why+is+alan+rickman+mean+to+me",
    "https://www.google.com/search?q=dude+this+jackson+guy+makes+awesome+exercises",
    "https://www.google.com/search?q=hallucinogenic+potions",
    "https://www.google.com/search?q=spell+to+make+my+dick+bigger",
    "https://www.google.com/search?q=horny+hogwarts+singles",
    "https://www.google.com/search?q=why+is+there+no+pokestops+at+hogwarts",
    "https://www.google.com/search?q=what+kind+of+parchment+does+a+pdf+use" ]

random_http = [
    "http://harrypotterfanzone.com/magical-creatures/",
    "http://hpotterfacts.tumblr.com/",
    "http://www.harrypotterwizardscollection.com/",
    "http://www.hoffmanrobes.com/",
    "http://www.thinkgeek.com/images/products/zoom/e83e_harry_potter_marauders_map.jpg",
    "http://harrypotter.wikia.com/wiki/Vanishing_Cabinet",
    "http://www.smosh.com/smosh-pit/articles/top-10-sexiest-wizards-harry-potter-1",
    "http://facebookpotter.tumblr.com/",
    "http://knowyourmeme.com/memes/snape-kills-dumbledore",
    "http://www.mugglenet.com/",
    "http://www.harrypotterfanclub.com/",
    "http://www.the-leaky-cauldron.org/",
    "http://www.hexrpg.com/" ]

random_ssl = [
    "https://en.wikipedia.org/wiki/Special:Random",
    "https://twitter.com/TheHPFacts",
    "https://www.pinterest.com/uptoolate16/harry-potter-facts/",
    "https://www.murphyrobes.com/",
    "https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom",
    "https://gist.github.com/graceavery/01ec404e555571a4a668c271c8f62e8b",
    "https://github.com/OpenHogwarts/hogwarts",
    "https://github.com/deedy/marauders-map",
    "https://www.facebook.com/HarryPotterUK",
    "https://twitter.com/_Snape_",
    "https://www.youtube.com/watch?v=lRSKCLXXMrk",
    "https://www.youtube.com/watch?v=F3YR1-gJjWM",
    "https://www.youtube.com/watch?v=ITqYqMNF4R8",
    "https://www.youtube.com/watch?v=6Tbffj_04cI" ]


def main():
    br = webdriver.Ie()

    while True:
        for i in [wiki_links, amazon_links, search_links,
                     random_http, random_ssl]:
            sleep(7)
            br.get(random.choice(i))


if __name__ == "__main__":
    main()
