i = 1
c = 0
while i<=5000:
	if i%5==0 and i%7==0:
		print("%d能被5和7整除"%i)
		c+=1
	i+=1
print("一共%d个"%c)
