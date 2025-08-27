'''Convert Snake Case to Pascal Case
Explanation: Change a snake_case string (words separated by underscores) into PascalCase (words start with uppercase, no underscores).
Input: "my_variable_name"
Expected Output: "MyVariableName"'''
def replace_to_pascal(s):
    # Replace underscores with spaces
    res = s.replace("_", " ")

    # Convert each word to Title Case (first letter capitalized)
    res = res.title()

    # Remove spaces to form PascalCase
    res = res.replace(" ", "")

    # Print the final PascalCase string
    print(res)

# Take snake_case string as input from user
s = input("Enter the string with snake_case: ")

# Call the function
replace_to_pascal(s)
