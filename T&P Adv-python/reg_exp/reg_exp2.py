import re
pattern=r"\d{2}-\d{2}-\d{4}"
text="Today's date start is 15-08-2021 and it will be end on 27-03-2026."
match=re.findall(pattern,text)
print(match)
