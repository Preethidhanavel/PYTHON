'''Convert Snake Case to Pascal Case
Explanation: Change a snake_case string (words separated by underscores) into PascalCase (words start with uppercase, no underscores).
Input: "my_variable_name"
Expected Output: "MyVariableName"'''
def replace_to_pascal(s):
    res = s.replace("_", " ").title().replace(" ", "")
    print(res)
s=input("Enter the string with snake_case:")
replace_to_pascal(s)