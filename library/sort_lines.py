with open(r"e:\classroom\python\aug2\names.txt","r") as f:
    lines = f.readlines()
    # convert list to set
    lines = set(lines)
    for name in sorted(lines):
        print(name, end='')

