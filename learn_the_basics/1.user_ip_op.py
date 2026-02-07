# taking user input -------- INPUTS ARE ALWAYS A STRING
name = input("Enter your name: ")

# printing output using print function
print("Hello, ", name, "! Welcome!")

print("Hello World")

# printing variables
s = "brad"
print(s)

s = "Angelina"
age = 25
city = "New York"
print(s, age, city)

# mulitple inputs
x, y, z = input("Enter three numbers: ").split() # INPUTS ARE STRING
print("Total number of students: ",z)
print("Number of boys: ", x)
print("Number of girls: ",y)
print(type(x), type(y), type(z)) # type() FOR GETTING TYPE OF VARIABLE INSIDE

# change type of input ---------TYPE CASTING
color = input("What color is rose?: ") # string input
print(color)
print(type(color))

n = int(input("How many roses?: ")) # TYPE CAST to integer
print(n)
print(type(n))

price = float(input("Price of each rose?: ")) # TYPE CAST to float
print(price)
print(type(price))