s1 = "hello"
s2 = "world"
common = set(s1) & set(s2)
res1 = "".join([c for c in s1 if c not in common])
res2 = "".join([c for c in s2 if c not in common])