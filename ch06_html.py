#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml.html import parse
from urllib2 import urlopen

parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))

doc = parsed.getroot()

links = doc.findall('.//a')

