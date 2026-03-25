import re
Pattern='^a...s$'
test_string='abyss'
result=re.match(Pattern,test_string)
if result:
    print("Search Successful")

print(result)