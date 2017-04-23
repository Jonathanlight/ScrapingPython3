#!/usr/bin/python3
import urllib
import requests
import os
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
from bs4 import BeautifulSoup
import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen


class Scraping:

    def __init__(self, url):
        self.url = url

    def runGet_href(self, namefile="href.txt"):
        soup = ""
        with urlopen(self.url) as url:
            htmltext = url.read()

        soup = BeautifulSoup(htmltext, "lxml")
        files = open(namefile,"w")

        for link in soup.find_all('a'):
            files.write(link.get('href')+'\n')
        files.close()
        print("done successfull href...")

    def runGet_img(self, namefile="image.txt"):
        soup = ""
        with urlopen(self.url) as url:
            htmltext = url.read()

        soup = BeautifulSoup(htmltext, "lxml")
        files = open(namefile,"w")

        for link in soup.find_all('img'):
            files.write(link.get('src')+'\n')
        files.close()
        print("done successfull img...")

    def runGet_meta(self, namefile="meta.txt"):
        soup = ""
        with urlopen(self.url) as url:
            htmltext = url.read()

        soup = BeautifulSoup(htmltext, "lxml")
        files = open(namefile,"w")

        for tag in soup.find_all("meta"):
            if tag.get('content') is not None:
                #print(tag.get('content'))
                files.write(tag.get('content')+'\n')
        files.close()
        print("done successfull meta...")

app = Scraping("https://www.youtube.com")
app.runGet_meta()
