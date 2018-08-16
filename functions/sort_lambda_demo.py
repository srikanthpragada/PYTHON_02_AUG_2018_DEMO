def get_len(s):
    return len(s)


names = ["Bill", "Tom", "Stephens", "Mike", "tim", "andy"]
for n in sorted(names, key=str.lower):
    print(n)

marks = {"Andy": 90, "Tom": 66, "Roberts": 80}
for t in sorted(marks.items(), key=lambda t: t[1]):
    print(t)
