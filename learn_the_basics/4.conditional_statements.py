

# IF
age = 20
if age >= 18:
    print("Eligible to vote.")

# IF-ELSE
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

# short hand if-else
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result : {res}")

# IF-ELIF-ELSE
age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# NESTED IF-ELSE
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# TERNARY CONDITIONAL
# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)


# MATCH-CASE
number = 2

match number:
    case 1:
        print("one")
    case 2|3:
        print("two or three")
    case _:
        print("other number")