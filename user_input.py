name = input("enter ur name :")
age =23.3
age = int(age)
age +=1
print(f"ur name is {name} ")
print(f"your age is {age}!")

# ex 1 : area of rectangle
w= int(input("enter the width of rectangle:"))
l =int(input("enter the length of rectangle:"))
A = w*l
print(f"the area of rectangle is {A}cm")


# shopping cart 
item = input("what would u like to buy :")
quantity = int(input("how many would u like to buy :"))
price = int (input("what is the price :"))
total =price * quantity

print(f"the tottal price is : {total} ")

# matlib games build a story by random words

noun =input("enter any noun :" )
noun2 =input("enter any noun2  :" )
adjective =input("enter any adjective to describe noun :")
verb =input("enter any verb ending should be 'ing' :")
print(f"my name is {noun}")
print (f"im very {adjective}")
print(f"im  currently  in {noun2} nd {verb}")