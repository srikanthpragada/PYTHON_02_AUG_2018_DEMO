set_m = set(dir(set))   # Convert a list to set
list_m = set(dir(list))

cm = set_m & list_m    # Intersection

for m in cm:
    if not m.startswith("__"):
        print(m)
