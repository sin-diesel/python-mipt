#!/usr/bin/env python3

from datetime import datetime as _datetime
from datetime import timedelta as _timedelta

def days_lived(year: int, month: int, day: int):
    birth_date = _datetime(year, month, day)
    now = _datetime.now()
    age = now - birth_date
    return age.days
