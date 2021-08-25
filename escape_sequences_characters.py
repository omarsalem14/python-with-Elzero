# ----------------------------------------------------
# Escape Sequences Characters
# \b => Back Space
# \New Line => Escape New Line + \
# \\Back Slash => Escape Back Slas
# \'' => Escape Single Qoute
# \"" => Escape Double Qoute
# \n => Line Feed Character
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value
# -------------------------------------------------------

# Back Space
print("Hello\bworld")  # Will Remove O

# Escape New Line + \
print("Hello \
I Love \
Python")

# Escape Back Slash
print("I Love Back Slash \\")

# Escape Single Qoute
print('I Love Single Qoute \'Test\'')

# Escape Double Qoute
print("I Love Single Qoute \"Test\"")

# Line Feed
print("Hello\nWorld!")  # Will Escape New line

# Carriage Return
print("123456\rABSDe")

# Horizontal Tab
print("Hello\tWorld")

# Character Hex Value
print("\x4F\x6D\x61\x72\t\x47\x7A\x65\x72\x61")  # Visit Letter hex value
