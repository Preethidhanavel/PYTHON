#What is typecasting? Provide examples where implicit and explicit type conversions may cause bugs.
#implicit
a = 3     
b = 2.5      
c = a + b    
print(c)     
print(type(c)) #float
#explicit
x = "abc"
y = int(x)    
print(y + 1) 
