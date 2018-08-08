st = "This is Python and it is a langauge!"
sub = "a"

pos = st.find(sub)
while pos >= 0:
    print(pos)
    pos = st.find(sub,pos+1)  # look for sub after previous occurrence

