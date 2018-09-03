from datetime import *

dobstr = input("Enter your date of birth (yyyymmdd) : ")
dob = datetime.strptime(dobstr, "%Y%m%d")
today = datetime.now()
diff = today - dob
years = diff.days // 365
months = diff.days % 365 // 30
days = diff.days - (years * 365 + months * 30)
print(years, ' year(s) ', months, ' month(s) ', days, ' day(s) ', ' old ')
