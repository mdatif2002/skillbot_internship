import file
fileread="fast.lib"
f=0
cell=[]
area=[]
pin=[]
pin_temp=[]
with open(fileread,"r") as readfile:
	file_con=readfile.read()
for line in file_con.split("\n"):
		m=re.match("cell ((.*)) {",line)
		m1=re.match("  area : (.*);",line)
		m2=re.match("  pin((.*))  {",line)
		if m:
			if f==1:
				pin.append(pin_temp)
				pin_temp=[]
			cell.append(m.group(1))
		elif m1:
			area.append(m1.group(1))
		elif m2:
			pin_temp.append(m2.group(1))
			f=1
pin.append(pin_temp)
for i in range(len(cell)):
	print(cell[i],area[i],pin[i])
