#!/usr/bin/env python

import json
import sys
import urllib2

from bs4 import BeautifulSoup

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
    print index, title, data.contents[2]
  else:
    foo[index]['descr'] = data.contents[-1]
    print index, title, data.contents[-1]

  if index % 10 == 0 or index == len(data_raw):
    try:
        print
        chosen = input("Select the input: ")
        print

        URL = "https://www.imdb.com%s" % foo[chosen]['url'] 

        oururl= urllib2.urlopen(URL).read()
        soup = BeautifulSoup(oururl, 'lxml')

        data = json.loads(soup.find('script', type='application/ld+json').text)

        print "title: ".ljust(20)   , data['name']

        if data.has_key('datePublished'):
            print "year: ".ljust(20)    , data['datePublished'].split("-")[0]

        if data.has_key('type'):
            print "type: ".ljust(20) , data['@type']

        print "url: ".ljust(20) , URL
        print "id: ".ljust(20) , URL.split('/')[-2]

        if data.has_key('description'):
            print "description: ".ljust(20), data['description']

        print
        sys.exit()

    except SyntaxError:
        print
        continue

