# --------------------------------------------
# --Strings Indexing And Slicing--
# [1] All Data in python is object
# [2] object contain Elements
# [3] Every Elements has its own Index
# [4] Python use zero based indexing (Index Start From zero)
# [5] Use square brackets to access Elements
# [6] Enable accessing parts of Strings, Tuple or Lists
# --------------------------------------------

# Indexing ( Access Single Item)

myString = "I Love python"

print(myString[0])  # Index 0 => I
print(myString[7])  # Index 6 => P

print(myString[-1])  # Index -1 => First Character from End
print(myString[-6])  # Index -6 => 6th Character from End

# slicing ( Access Multiple Sequence Items)
# [Start:End] If End Mentioned Its not Included
# Syntax [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:11])  # If Start not included the defualt will run [Start:11]
print(myString[8:])  # If End not included the defualt will run [8:End]
print(myString[:])  # Full Data

print(myString[0::1])  # Full Data
print(myString[::2])  # Steps is mean Skip 2 Staps #Ilv yhn
