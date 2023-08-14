import re
fileread="fast.lib"
f=0
cell=[]
area=[]
pin=[]
pin_temp=[]
with open(fileread,"r") as readfile:
	file_con=readfile.read()
for line in file_con.split("\n"):
		matched=re.match("cell ((.*)) {",line)
		matched1=re.match("  area : (.*);",line)
		matched2=re.match("  pin((.*))  {",line)
		if matched:
			if f==1:
				pin.append(pin_temp)
				pin_temp=[]
			cell.append(matched.group(1))
		elif matched1:
			area.append(matched1.group(1))
		elif matched2:
			pin_temp.append(matched2.group(1))
			f=1
pin.append(pin_temp)
for i in range(len(cell)):
	print(cell[i],area[i],pin[i])
