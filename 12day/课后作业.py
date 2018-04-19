list = []
while True:
		#输入
		name = input("请输入你的名字")
		age = input("请输入你的年龄")
		sex = input("请输入你的性别")
		qq = input("请输入你的qq")
		weight =float(input("请输入你的体重"))
	#字典赋值
		if name not in name_list:	
		dict["name"]= name
		dict["age"]= age
		dict["sex"]= sex
		dict["qq"]= qq
		dict["weight"]= weight

		#list = [{}]
		#int float str bool list tuple dictionary
		list.append(dict)
		print("list")
