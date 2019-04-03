#!/usr/bin/env python

import json
import sys
import urllib2

from bs4 import BeautifulSoup

URL = 'https://www.imdb.com/find?q=%s&s=tt' % sys.argv[1]
oururl= urllib2.urlopen(URL).read()
soup = BeautifulSoup(oururl, 'lxml')

foo = {}

data_raw = soup.find_all('td', class_='result_text')

for data in data_raw:
  index = data_raw.index(data)

  foo[index] = {}

  url   = data.find('a')['href'].split('?')[0]
  title = data.find('a').contents[0]

  foo[index]['url'] = url
  foo[index]['title'] = title

  small =  data.find('span', class_='ghost')

  if small:
    foo[index]['descr'] = data.contents[2]
    print index, url, title, data.contents[2]
  else:
    foo[index]['descr'] = data.contents[-1]
    print index, url, title, data.contents[-1]

print

chosen = input("Select the input: ")

print

URL = "https://www.imdb.com%s" % foo[chosen]['url'] 


oururl= urllib2.urlopen(URL).read()
soup = BeautifulSoup(oururl, 'lxml')

data = json.loads(soup.find('script', type='application/ld+json').text)

print "title :"   , data['name']

if data.has_key('datePublished'):
  print "year :"    , data['datePublished'].split("-")[0]


if data.has_key('type'):
  print "type :" , data['@type']

print "url :" , URL
print "id :" , URL.split('/')[-2]

if data.has_key('description'):
  print "description :", data['description']

print
