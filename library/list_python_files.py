import os


def print_file(dirname,filename):
    fullname = dirname + '\\'+ filename
    print("\n*****   {0}  ******\n" .format(fullname))
    with open(fullname) as file:
        for line in file:
            print(line, end='')


allfiles = os.walk(r"e:\classroom\python\aug2")

for (dirname,directories,files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            print_file(dirname, f)
