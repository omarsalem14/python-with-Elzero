# ------------------------------------------------------
# --variables --
# ----------------
# syntax => [Variable Name] [Assigment Operator] [Value]
#
# Name Convention and Rules
# [1]Cant start with (a-z  A-Z) or Underscore
# [2]I Can't begin with number or Special Charecters {2myVariable},{-myVariable}
# [3]Can include (0-9) or Underscore
# [4]Can't include special characters {=my-Variable}
# [5]Name is not like name [case sensetive]= MyVariable"The Variable"    print(myVariable)
# Variable must assigne firstly then u can  print it :
# print(myVariable)
# myVariable = "The Variable"
# ------------------------------------------------------

myVariable = "The Variable"
print(myVariable)
MyVariable = "The Variable"
print(MyVariable)
_myVariable = "The Variable"
print(_myVariable)

my100_Variable = "The Variable"
print(my100_Variable)

name = "Omar Gzera"  # single word =>Normal
myName = "Omar Gzera"  # two word =>camelCase
my_name = "Omar Gzera"  # two word =>snake_case
print("name")
print("myName")
print("my_name")
