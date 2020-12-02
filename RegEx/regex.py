import re

data = """
Lorem ipsum dolor sit amet, consectetur 
adipiscing elit, sed BK-N130531 do eiusmod tempor incididunt 
ut labore et dolore magna aliqua. Ut enim ad minim 
veniam, quis nostrud exercitation ullamco laboris nisi 
ut aliquip AB-N175236 ex ea YB-N5319 commodo consequat. Duis aute irure 
dolor in reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. JD-N830532 Excepteur sint occaecat
 cupidatat UV-N950432 non proident, sunt in culpa qui officia 
 deserunt mollit anim id YU-N84319 est laborum.
"""

# Compile the patterns, the expression here means:
# 2 Alphabets +
# a Dash +
# literal `N` +
# 6 Digits
pattern = re.compile(r"[A-Z]{2}-N\d{5,6}")

# Find all the string that matches the pattern,
# and return it as a list
found_ids = pattern.findall(data)

# Iterate ^.^
for i in found_ids:
    print(i)