'''Detect URLs Within a String
Explanation: Extract all URLs from the string.
Input: "Check this link: https://openai.com and http://github.com"
Expected Output: URLs found: ['https://openai.com', 'http://github.com']'''
import re

def extractURL(s):
    url_list = []
    regex = r'\b((?:https?|ftp|file):\/\/[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#\/%=~_|])'
    p = re.compile(regex, re.IGNORECASE)
    m = p.finditer(s)
    for match in m:
        url_list.append(s[match.start():match.end()])
    if len(url_list) == 0:
        print("-1")
        return
    for url in url_list:
        print(url)


string = input("Enter the string having URL:")
extractURL(string)
