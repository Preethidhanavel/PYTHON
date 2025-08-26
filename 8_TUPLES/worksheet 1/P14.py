'''Description: Convert a tuple of characters to a string and then back to a tuple.
Useful for text manipulation and transitioning between data representations.
Input: t = ('P', 'y', 't', 'h', 'o', 'n')
Output: String: "Python"
Tuple: ('P', 'y', 't', 'h', 'o', 'n')'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
print("The string :",''.join(t))
print("The tuple:",t)
