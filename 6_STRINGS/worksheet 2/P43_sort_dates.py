'''Sort List of Dates Given as Strings
Explanation: Sort dates given as strings in chronological order.
Input: ["2021-05-21", "2019-01-12", "2020-12-15"]
Expected Output: ['2019-01-12', '2020-12-15', '2021-05-21']'''
from datetime import datetime

# List of dates in string format
dates = ["24 Jul 2017", "25 Jul 2017", "11 Jun 1996", "01 Jan 2019", "12 Aug 2005", "01 Jan 1997"]

# Sort the list using datetime objects for proper date comparison
# datetime.strptime() converts string date to datetime object
dates.sort(key=lambda x: datetime.strptime(x, '%d %b %Y'))

# Print the sorted list
print(dates)
