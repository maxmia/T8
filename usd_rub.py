#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import datetime

from xml.sax import parseString
from xml.sax.handler import ContentHandler

from couchdb import Server

RATE_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
server = Server("http://localhost:5984")

rate = server["rate"]
valute = server["valute"]


class CurrHandler(ContentHandler):

    date = None
    name = None
    valute = {}

    def startElement(self, name, attrs):
        if name == 'Valute':
            self.valute = {}
        elif name == 'ValCurs':
            d,m,y = map(int,attrs['Date'].split('.'))
            self.date = datetime.date(y,m,d)
        else:
            self.name = name

    def endElement(self, name):
        if name == 'Valute':
            self.feed_valute(self.valute)
            self.valute = {}

    def characters(self, content):
        if self.name and content:
            self.valute[str(self.name.lower())] = content
            self.name = None

    def feed_valute(self, _valute):
        f = lambda x: float(x.replace(',','.'))
        id = _valute['charcode']
        v = rate.get(id, {'_id':id})
        v["date"] = self.date.toordinal(),
        v["nominal"] = f(_valute['nominal'])
        v["value"] = f(_valute['value'])
        rate.save(v)
        
        if not id in valute:
            valute.save({
              '_id': id,
              'name': _valute['name'],
              'active': False,
            })


if not 'RUB' in rate:
    rate.save({
              '_id': "RUB",
              'date': 0,
              'nominal': 1,
              'value': 1,
            })
            
f = urllib.urlopen(RATE_URL)
raw_data = f.read()

handler = CurrHandler()
parseString(raw_data, handler)
