import os
import unittest
from .core import moment


class MomentTest(unittest.TestCase):


    def test_date_format(self):
        self.assertEqual("2012-12-18", moment.date("12-18-2012").format("YYYY-M-D"))
        self.assertEqual("18-12-2012", moment.date("12-18-2012").format("DD-M-YYYY"))
        self.assertEqual("12-18-2012", moment.date("12-18-2012").format("M-D-YYYY"))
        
    def test_date_strftime(self):
        self.assertEqual("2012-12-18",moment.date(2012, 12, 18).strftime("%Y-%m-%d") )
    
    def test_utc_time(self):
        self.assertEqual("2012-12-19", moment.unix(1355875153626).format("YYYY-M-D"))
        self.assertEqual("19-12-2012", moment.unix(1355875153626).format("DD-M-YYYY"))
        self.assertEqual("12-19-2012", moment.unix(1355875153626).format("M-D-YYYY"))

    def test_day_format(self):
        self.assertEqual("Thursday", moment.date("2017-09-28T21:45:23Z").format("dddd"))
    
    def test_day_format_month(self):
        self.assertEqual(9, moment.date("2017-09-28T21:45:23Z").month)

    def test_day_format_day(self):
        self.assertEqual(28, moment.date("2017-09-28T21:45:23Z").day)
    
    def test_day_format_year(self):
        self.assertEqual(2017, moment.date("2017-09-28T21:45:23Z").year)
        
    def test_chaining(self):
        self.assertEqual("2012-12-09", moment.date(2012, 12, 19).replace(weekday=-7).format("YYYY-MM-DD"))
    
    def test_adding_hours(self):
        self.assertEqual("2016-02-09 12:00 AM", moment.date("2012-12-09").add(years=3, months=2).format("YYYY-M-D h:m A"))


if __name__ == "__main__":
    unittest.main()