"""Create a function that returns a list of a given size of date objects
that correspond to week days starting at a given date.

Created on 17 Feb 2016

@author: paulross
"""
from calendar import weekday
import datetime

import pytest

def business_days(start_date, num):
    test = start_date # datetime.date(2016, 1, 1)
    # weekday(test)
    # test.weekday()
    a = [test + datetime.timedelta(days=i) for i in range(num*2)]
    # list(map(lambda x: x.weekday() == 1, a))
    b = list(map(lambda x: x.weekday() in (5,6), a))
    c = []
    for i in range(num*2):
        if b[i] == False: 
            c.append(a[i])
    return c[:num]


def test_business_days():
    start_date = datetime.date(2016, 1, 1)
    result = business_days(start_date, 10)
    expected = [
        datetime.date(2016, 1, 1),
        datetime.date(2016, 1, 4), 
        # datetime.date(2016, 1, 4).isoweekday() # Monday is 1 
        # datetime.date(2016, 1, 4).strftime('%A'))
        datetime.date(2016, 1, 5),
        datetime.date(2016, 1, 6),
        datetime.date(2016, 1, 7),
        datetime.date(2016, 1, 8),
        datetime.date(2016, 1, 11),
        datetime.date(2016, 1, 12),
        datetime.date(2016, 1, 13),
        datetime.date(2016, 1, 14),
    ]
    assert result == expected


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
    
