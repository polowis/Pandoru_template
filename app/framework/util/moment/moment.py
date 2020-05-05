from .date import MutableDate

from calendar import timegm
from datetime import datetime, timedelta
from time import timezone

import pytz
import times
from datetime import datetime

import dateparser
import sys

STRING_TYPES = (basestring, ) if sys.version_info < (3, 0) else (str, )

def parse_date_and_formula(*args):
    """Doesn't need to be part of core Moment class."""
    date, formula = _parse_arguments(*args)
    parse_settings = {"PREFER_DAY_OF_MONTH": "first"}
    if date and formula:
        if isinstance(date, datetime):
            return date, formula
        if '%' not in formula:
            formula = parse_js_date(formula)
        date = dateparser.parse(date, date_formats=[formula], settings=parse_settings)
    elif isinstance(date, list) or isinstance(date, tuple):
        if len(date) == 1:
            # Python datetime needs the month and day, too.
            date = [date[0], 1, 1]
        date = datetime(*date)
    elif isinstance(date, STRING_TYPES):
        date = dateparser.parse(date, settings=parse_settings)
        formula= "%Y-%m-%dT%H:%M:%S"
    return date, formula


def _parse_arguments(*args):
    """Because I'm not particularly Pythonic."""
    formula = None
    if len(args) == 1:
        date = args[0]
    elif len(args) == 2:
        date, formula = args
    else:
        date = args
    return date, formula


def parse_js_date(date, obj = None):
    # AM/PM
    if 'A' in date:
        date = date.replace('A', '%p')
    elif 'a' in date:
        date = date.replace('a', '%P')
    # 24 hours
    if 'HH' in date:
        date = date.replace('HH', '%H')
    elif 'H' in date:
        date = date.replace('H', '%k')
    # 12 hours
    elif 'hh' in date:
        date = date.replace('hh', '%I')
    elif 'h' in date:
        date = date.replace('h', '%l')
    # Minutes
    if 'mm' in date:
        date = date.replace('mm', '%min')
    elif 'm' in date:
        date = date.replace('m', '%min')
    # Seconds
    if 'ss' in date:
        date = date.replace('ss', '%S')
    elif 's' in date:
        date = date.replace('s', '%S')

    # Milliseconds
    if 'SSS' in date:
        date = date.replace('SSS', '%3')

    # Years
    if 'YYYY' in date:
        date = date.replace('YYYY', '%Y')
    elif 'YY' in date:
        date = date.replace('YY', '%y')

    # Months
    if 'MMMM' in date:
        date = date.replace('MMMM', '%B')
    elif 'MMM' in date:
        date = date.replace('MMM', '%b')
    elif 'MM' in date:
        date = date.replace('MM', '%m')
    elif 'M' in date:
        date = date.replace('M', '%m')

    # Days of the week
    if 'dddd' in date:
        date = date.replace('dddd', '%A')
    elif 'ddd' in date:
        date = date.replace('ddd', '%a')
    elif 'dd' in date:
        date = date.replace('dd', '%w')
    elif 'd' in date:
        date = date.replace('d', '%u')

    # Days of the year

    if 'DDDD' in date:
        date = date.replace('DDDD', '%j')
    elif 'DDD' in date:
        date = date.replace('DDD', '%j')
    # Days of the month
    elif 'DD' in date:
        date = date.replace('DD', '%d')
    elif 'D' in date:
        date = date.replace('D', '%d')

    if 'LLLL' in date:
        date = date.replace('LLLL', "%A, " +str(obj._date.strftime("%B"))+" %d, %Y %H:%min PM")
    elif 'LLL' in date:
        date = date.replace('LLL', str(obj._date.strftime("%B"))+" %d, %Y %H:%min PM")
    elif 'LL' in date:
        date = date.replace('LL',  str(obj._date.strftime("%B"))+" %d, %Y")
    elif 'L' in date:
        date = date.replace('L', '%m/%d/%Y')

    if '%min' in date:
        date = date.replace('%min', '%M')
    return date

def format_if_lower_than_1(number, keyword):
    if int(number) < 1:
        return ""
    if int(number) == 1:
        return str(number) + " " + keyword
    else: 
        return str(number) + " " + keyword + "s"

class Moment(MutableDate):
    """Date class"""
    def __init__(self, *args):
        date, formula = parse_date_and_formula(*args)
        self._date = date
        self._formula = formula
    
    @classmethod
    def now(cls):
        date = datetime.now()
        formula = "%Y-%m-%dT%H:%M:%S"
        return cls(date, formula)
    
    @classmethod
    def utc(cls, *args):
        """Create a moment from a UTC date."""
        date, formula = parse_date_and_formula(*args)
        date = pytz.timezone("UTC").localize(date)
        return cls(date, formula)

    @classmethod
    def utcnow(cls):
        """UTC equivalent to now."""
        date = pytz.timezone("UTC").localize(datetime.utcnow())
        formula = "%Y-%m-%dT%H:%M:%S"
        return cls(date, formula)

    @classmethod
    def unix(cls, timestamp, utc=False):
        """Create a date from a Unix timestamp."""
        # Which function are we using?
        if utc:
            func = datetime.utcfromtimestamp
        else:
            func = datetime.fromtimestamp
        try:
            # Seconds since epoch
            date = func(timestamp)
        except ValueError:
            # Milliseconds since epoch
            date = func(timestamp / 1000)
        # Feel like it's crazy this isn't default, but whatever.
        if utc:
            date = date.replace(tzinfo=pytz.utc)
        formula = "%Y-%m-%dT%H:%M:%S"
        return cls(date, formula)

    def locale(self, zone=None):
        """Explicitly set the time zone you want to work with."""
        if not zone:
            self._date = datetime.fromtimestamp(timegm(self._date.timetuple()))
        else:
            try:
                self._date = pytz.timezone(zone).normalize(self._date)
            except ValueError:
                self._date = self._date.replace(tzinfo=pytz.timezone(zone))
        return self

    def timezone(self, zone):
        """
        Change the time zone and affect the current moment's time. Note, a
        locality must already be set.
        """
        date = self._date
        try:
            date = times.to_local(times.to_universal(date), zone)
        except:
            date = times.to_local(date, zone)
        finally:
            self._date = date
        return self

    def format(self, formula):
        """Display the moment in a given format."""
        formula = parse_js_date(formula, self)
        return self._date.strftime(formula)

    def fromNow(self):
        current = self.now()
        print(current)
        time = current.subtract(hours=self._date.hour, minutes=self._date.minute, seconds=self._date.second, years=self._date.year, months=self._date.month)
        year = time.format("YY")
        months = time.format("m")
        hours = time.format("h")
        return format_if_lower_than_1(year, "year") + " " + format_if_lower_than_1(months, "month") + " " + format_if_lower_than_1(hours, "hour") + " ago"



    def strftime(self, formula):
        return self._date.strftime(formula)

    def diff(self, moment, measurement=None):
        """Return the difference between moments."""
        return self - moment

    def done(self):
        """Return the datetime representation."""
        return self._date

    def clone(self):
        """Return a clone of the current moment."""
        clone = Moment(self._date)
        clone._formula = self._formula
        return clone

    def copy(self):
        return self.clone()

    def __repr__(self):
        if self._date is not None:
            formatted = self._date.strftime("%Y-%m-%dT%H:%M:%S")
            return "<Moment(%s)>" % (formatted)
        return "<Moment>"

    def __str__(self):
        formatted = self._date.strftime("%Y-%m-%dT%H:%M:%S")
        tz = str.format("{0:+06.2f}", -float(timezone) / 3600)
        return formatted + tz
    
