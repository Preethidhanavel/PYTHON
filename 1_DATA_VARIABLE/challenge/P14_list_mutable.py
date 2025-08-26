#Describe what happens in memory when you do
a = [1, 2, 3]   # A list object [1,2,3] is created in memory, 'a' points to it
b = a           # 'b' is assigned the SAME reference as 'a' (both point to same list)
b[0] = 10       # Change first element of list -> since list is mutable, the change 
                # is visible through both 'a' and 'b'
print(a)        # Output: [10, 2, 3] -> because 'a' and 'b' share the same object
