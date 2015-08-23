""" Generic utility functions """
import parsedatetime
import datetime


def parse_date(date):
    """
    Receives string date, Returns tuple of string date, sortable date,
    shortened date
    """
    months = {1: 'Jan',
              2: 'Feb',
              3: 'Mar',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'Aug',
              9: 'Sept',
              10: 'Oct',
              11: 'Nov',
              12: 'Dec',
              }
    pdt = parsedatetime.Calendar()
    sort_date, t = pdt.parse(date)
    year = str(sort_date[0])
    month = months[sort_date[1]]
    day = str(sort_date[2])

    date_obj = datetime.date(sort_date[0], sort_date[1], sort_date[2])
    pub_date = date_obj.strftime("%a, %d %b %Y %H:%M:%S GMT")

    if len(day) > 1 and day[0] == '1':
        suffix = 'th'
    elif day[-1] == '1':
        suffix = 'st'
    elif day[-1] == '2':
        suffix = 'nd'
    elif day[-1] == '3':
        suffix = 'rd'
    else:
        suffix = 'th'

    date = "%(month)s %(day)s%(suffix)s %(year)s" % {
        'month': month,
        'day': day,
        'suffix': suffix,
        'year': year,
        }

    return date, sort_date, pub_date
