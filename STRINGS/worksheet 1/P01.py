'''Check if a String is a Palindrome or Symmetrical
Explanation: A palindrome reads the same forwards and backwards (e.g., "madam"). A symmetrical string has matching halves.
Input: "madam"
Expected Output:
Palindrome: Yes
Symmetrical: Yes'''


def check_pal_sym(s):
    mid = len(s) // 2
    pal = s == s[::-1]

    if len(s) % 2 == 0:
        left = s[:mid]
        right = s[mid:]
    else:
        left = s[:mid]
        right = s[mid+1:]
    sym = left == right

    return pal, sym


s = input("Enter the string: ")

is_pal, is_sym = check_pal_sym(s)

print("Palindrome:", "Yes" if is_pal else "No")
print("Symmetrical:", "Yes" if is_sym else "No")

