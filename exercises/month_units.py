# Display no. of units sold in each month
sales = {}

while True:
    month = int(input("Enter month :"))
    if month == 0:
        break

    qty = int(input("Enter quantity : "))
    if month in sales:
        sales[month] = sales[month] + qty   # Update existing entry
    else:
        sales[month] = qty      # Add new entry

for m, q in sorted(sales.items()):
    print("%3d  %5d" % (m, q))
