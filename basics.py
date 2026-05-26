# comments 
# This is a single-line comment
print("Hello, world!")  # This comment is after code
 

'''
This is also used
as a multiline comment
in Python
'''

 
# variables : variable is a named container used to store value (interger,float,boolean,string) in a program.
# variable behaves as if it wasthe value it contains


# string variable
name ="divya"
print (name)
print("name")
print(f"the name is : {name}") # this is called f-string
name2 = "yadav"
message = name +""+name2


# integer variable
age = 20
print(f"My name is {name2} and I am {age} years old.")
# Float variable 
price = 99.99
temperature = 36.5
print(f"the price and temp are : {price} , {temperature}")
# boolean variable 
is_student = True
is_logged_in = False
print(f"are u logged in:{is_logged_in}")

if is_student:
    print("u are a student")
else:
    print("u are not")  
# dictionary 
a = {'name':'divya''neha''shruti',
     age : 2345,
     'city' : "dhule" "nashik"     }   

#tuple --immutable 
student =("divya",32,"information technology")

#list -- mutable 
name =["eva","adhira","anvi"]
no =[3,4,4]
 
# to find type of variable
x = 10
print(type(x))