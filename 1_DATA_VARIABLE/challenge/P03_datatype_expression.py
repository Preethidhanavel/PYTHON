#What is the output and data type of the expression: 3 + 4.0 * 2 // 3? Explain each step.
x = 3 + 4.0 * 2 // 3
# 1) 4.0 * 2   -> 8.0        (float * int = float)
# 2) 8.0 // 3  -> 2.0        (floor division with float returns float)
# 3) 3 + 2.0   -> 5.0        (int + float = float)

print(x, type(x))  # Output: 5.0 <class 'float'>