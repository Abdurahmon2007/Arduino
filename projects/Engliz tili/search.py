import re

malumot = "Ismi Abduraxmon"
x = re.search("^.*Abduraxmon$", malumot)

if x:
	print("Malumot topildi")
else: 
	print("Malumot topilmadi")