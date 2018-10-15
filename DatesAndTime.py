# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:35:59 2018

@author: Anton
"""

import datetime
import calendar

print(calendar.isleap(2018))

d = datetime.date(2016, 7, 24)
tday = datetime.date.today()
tday.year
tday.isoweekday()

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)


t = datetime.time

t.hour