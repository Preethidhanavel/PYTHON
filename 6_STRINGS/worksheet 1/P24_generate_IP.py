'''Generate All Valid IP Addresses from a String
Explanation: Given a string of digits, form all possible valid IP addresses.
Input: "25525511135"
Expected Output: ['255.255.11.135', '255.255.111.35']'''
# Function to check if a string is a valid part of an IP address
def isValid(s):
    n = len(s)
    if n == 1:
        return True
    val = int(s)
    # A valid segment must not start with '0' (unless it's "0") and must be ≤ 255
    if s[0] == '0' or val > 255:
        return False
    return True


# Recursive function to generate IP addresses
def generateIpRec(s, index, curr, cnt, res):
    temp = ""
    # If we have already processed all characters, stop
    if index >= len(s):
        return

    # If 3 dots already placed, check the last segment
    if cnt == 3:
        temp = s[index:]  # Take the remaining string
        if len(temp) <= 3 and isValid(temp):
            res.append(curr + temp)  # Add full IP address
        return

    # Try placing a dot after 1, 2, or 3 digits
    for i in range(index, min(index + 3, len(s))):
        temp += s[i]
        if isValid(temp):
            # Recurse with updated index, current IP, and dot count
            generateIpRec(s, i + 1, curr + temp + ".", cnt + 1, res)


# Wrapper function to generate all valid IP addresses
def generateIp(s):
    res = []
    generateIpRec(s, 0, "", 0, res)
    return res


# ---- Main Program ----
s = input("Enter the string: ")

# Generate valid IPs
res = generateIp(s)

# Print all possible IP addresses
for ip in res:
    print(ip)

