set_a = {1, 2}
set_b = {1, 2, 3, 4}
is_subset = True
for element in set_a:
    if element not in set_b:
        is_subset = False
        break