#!/usr/bin/python
#  -*- coding: utf-8 -*-
# USD/RUB CBR Ret  

from urllib2 import urlopen
from xml.etree import ElementTree as etree

with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=10) as r:
    print(etree.parse(r).findtext('.//Valute[@ID="R01235"]/Value'))
