#!/usr/bin/env python

import sys
import urllib2

from bs4 import BeautifulSoup

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

URL = 'https://www.imdb.com/find?q=%s&s=tt' % urllib2.quote(sys.argv[1])
print
print "Searching via %s" % URL
oururl= urllib2.urlopen(URL).read()
soup = BeautifulSoup(oururl, 'lxml')

foo = {}

data_raw = soup.find_all('td', class_='result_text')

print
print "%s result(s) - Just press ENTER to page trough results" % len(data_raw)
print

while True:

    for data in data_raw:

      index = data_raw.index(data) + 1

      foo[index] = {}

      url   = data.find('a')['href'].split('?')[0]
      title = data.find('a').contents[0]

      foo[index]['url'] = url
      foo[index]['title'] = title

      small =  data.find('span', class_='ghost')

      if small:
        foo[index]['descr'] = data.contents[2]
        print bcolors.WARNING + str(index) + ")" + bcolors.ENDC, title, data.contents[2]
      else:
        foo[index]['descr'] = data.contents[-1]
        print bcolors.WARNING + str(index) + ")" + bcolors.ENDC, title, data.contents[-1]

      if index % 10 == 0 or index == len(data_raw):
        try:
            print
            chosen = input("Select the input: ")
            print

            URL = "https://www.imdb.com%s" % foo[chosen]['url'] 

            URL_AKAS = URL + "releaseinfo"

            oururl= urllib2.urlopen(URL).read()
            soup = BeautifulSoup(oururl, 'lxml')

            oururl2= urllib2.urlopen(URL_AKAS).read()
            soup2 = BeautifulSoup(oururl2, 'lxml')

            # <td class="aka-item__title">

            akas = soup2.find_all('td', class_='aka-item__title')

            bla = set(akas)

            # <div class="originalTitle">
            orig_title_found = soup.find('div', class_='originalTitle')
            if orig_title_found:
              orig_title = orig_title_found.contents[0]
            else:
              orig_title = ""

            # <span id="titleYear">
            year_found = soup.find('span', id='titleYear')
            if year_found:
              year = year_found.text
            else:
              year = ""

            # <meta property='og:title' content="Devdas (2002) - IMDb" />
            title = soup.find('meta', property='og:title')

            #  <div class="summary_text">
            summary = soup.find('div', class_='summary_text').contents[0].strip()

            print bcolors.OKGREEN + "title: ".ljust(20) + bcolors.ENDC, bcolors.FAIL + title['content'].replace(" - IMDb", "") + bcolors.ENDC
            print bcolors.OKGREEN +  "title_orig: ".ljust(20) + bcolors.ENDC , bcolors.FAIL + orig_title + bcolors.ENDC

            print bcolors.OKGREEN + "year: ".ljust(20)  + bcolors.ENDC   , bcolors.FAIL +  year.strip("(").strip(")") + bcolors.ENDC

            print bcolors.OKGREEN + "url: ".ljust(20) + bcolors.ENDC , bcolors.FAIL + URL + bcolors.ENDC
            print bcolors.OKGREEN +  "id: ".ljust(20) + bcolors.ENDC , bcolors.FAIL + URL.split('/')[-2] + bcolors.ENDC

            for aka in bla:
              print bcolors.OKGREEN +  "title_aka: ".ljust(20) + bcolors.ENDC, bcolors.FAIL + aka.text + bcolors.ENDC

            print bcolors.OKGREEN +  "summary: ".ljust(20) + bcolors.ENDC, bcolors.FAIL + summary + bcolors.ENDC

            print

        except SyntaxError:
            print
            continue

