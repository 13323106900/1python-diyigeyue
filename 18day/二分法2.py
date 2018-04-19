list =[1,2,3,4,5,6,7,8,9]
key=6
center=int(len(list)/2)
if key in list:
	while True:
		if list[center]>key:
			center=center-1
		elif list[center]<key:
			center=center+1
		elif list[center]==key:
			print("要找的数字是%d在索引%d"%(key,center))
			break







