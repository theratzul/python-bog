#!/usr/bin/python3

import calendar
from datetime import date

# Get today's date
today = date.today()

yy = today.year
mm = today.month

print(calendar.month(yy, mm ))