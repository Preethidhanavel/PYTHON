'''Sort List of Dates Given as Strings
Explanation: Sort dates given as strings in chronological order.
Input: ["2021-05-21", "2019-01-12", "2020-12-15"]
Expected Output: ['2019-01-12', '2020-12-15', '2021-05-21']'''
from datetime import datetime


dates = ["24 Jul 2017", "25 Jul 2017", "11 Jun 1996", "01 Jan 2019", "12 Aug 2005", "01 Jan 1997"]
dates.sort(key=lambda x: datetime.strptime(x, '%d %b %Y'))
print(dates)