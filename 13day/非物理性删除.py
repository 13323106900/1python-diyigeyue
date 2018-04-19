list = [{"name":"a","isdelete":0},{"name":"b","isdelete":"0"}]
name = input("请输入要删除的名字")
for temp in list:
		if name ==temp["name"]:
			temp["isdelete"] = 1

for temp in list:
		if temp["isdelete"] ==0:
			print(temp)
