'''Detect URLs Within a String
Explanation: Extract all URLs from the string.
Input: "Check this link: https://openai.com and http://github.com"
Expected Output: URLs found: ['https://openai.com', 'http://github.com']'''
import re

# Function to extract URLs from a string
def extractURL(s):
    url_list = []  # List to store extracted URLs

    # Regex pattern to match http, https, ftp, or file URLs
    regex = r'\b((?:https?|ftp|file):\/\/[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#\/%=~_|])'
    
    # Compile the regex pattern (case-insensitive)
    p = re.compile(regex, re.IGNORECASE)
    
    # Find all matches of URLs in the string
    m = p.finditer(s)
    for match in m:
        url_list.append(s[match.start():match.end()])  # Extract and append URL
    
    # If no URL is found, print -1
    if len(url_list) == 0:
        print("-1")
        return
    
    # Print all extracted URLs
    for url in url_list:
        print(url)


# Take input from the user
string = input("Enter the string having URL: ")

# Call the function
extractURL(string)

