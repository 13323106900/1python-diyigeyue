list=[1,2,4,5,7,8,10,12,16]
key=8
center=int(len(list)/2)
if key in list:
	while True:
		if list[center]>key:
			center=center-1
		elif list[center]<key:
			center=center+1
		elif list[center] == key:
			print("要找的数字是%d在索引%d"%(key,center))
			break


