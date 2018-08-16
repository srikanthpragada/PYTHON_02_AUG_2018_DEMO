# Display no. of units sold in each month
sales = {}

while True:
    month = int(input("Enter month :"))
    if month == 0:
        break

    qty = int(input("Enter quantity : "))
    if month in sales:
        sales[month].append(qty)
    else:
        sales[month] = [qty]     # Add new entry

for m, q in sorted(sales.items()):
    print(m, q)
