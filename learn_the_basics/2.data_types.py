# NUMERIC DATA TYPE
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

# SEQUENCE DATA TYPE - ordered collection of items
s = "hello world" # string
print(type(s))

print(s[0]) # accessing string with index
print(s[1])
print(s[-1])

a = [] # empty list

a = [1, 2, 3] # list with integer values
print(a)

b = ["geeks", "for", "geeks", 4, 5] # list with mixed values
print(b)

print(a[0]) # access list items
print(a[1])
print(a[2])

# tuple data type - immutable
tup1 = () # initiate empty tuple

tup2 = ("Geeks", "for")
print("\nTuple with the use of strings: ", tup2)

tup1 = (1,2,3,4,5)
print(tup1[0]) # access tuple items
print(tup1[1])
print(tup1[2])

# BOOLEAN DATA TYPE
print(type(True))
print(type(False))

if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")

# SET DATA TYPE - unordered collection of items - mutable and no duplicate elements
# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

set1 = set(["Geeks", "For", "Geeks"]) #Duplicates are removed automatically
print(set1) 

# loop through set
for i in set1:
   print(i, end=" ") #prints elements one by one

print()

# check if item exist in set   
print("Geeks" in set1)

# DICTIONARY DATA TYPE - used for map - key-value pair
# initialize empty dictionary
d = {}

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

# Accessing an element using key
print(d[2])

# Accessing a element using get
print(d.get(3))
