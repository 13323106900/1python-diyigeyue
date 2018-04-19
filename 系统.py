#输入密码
print("户口".center(30,"*"))
print("1:新增人口".center(30," "))
print("2:查找人口".center(30," "))
print("3:修改人口".center(30," "))
print("4:删除人口".center(30," "))
cards =[]#定义空列表
while True:
		fun_number =int(input("请选择功能"))
		if fun_number ==1:
				print("新增")
				flag=0#默认值　0代表不在里面
				card={}#定义空字典
				name = input("请输入名字")
				for temp in  cards:
						if name == temp["name"]:
								flag=1#在里面
								break
						#[{1},{2},{3}]
				if flag ==1:#重复了直接结束当次循环，继续下次循环
						print("名字重复了")
						continue
				birthday = input("请输入出生日期")
				home=input("请输入籍贯")
				race = input("请输入民族")
				relation=input("请输入与户主的关系")
				sex=input("请输入性别")	
				#[{},{},{},{}]
				#if flag ==0:#走到这里flag一定等于0
				card["name"]=name
				card["birthday"]=birthday				
				card["home"]=home
				card["race"]=race
				card["relation"]=relation
				card["sex"]=sex
				#放到列表中
				cards.append(card)
				print("新增成功")
		elif fun_number ==2:
				name=input("请输入要查找的姓名")
				flag=0#假设不在里面
				count=0#默认找到了零次
				for temp in cards:
						count+=1#记录找的次数
						if name ==temp["name"]:
								flag = 1
								#print("姓名:%s\n出生日期:%s\n籍贯:%s\n民族:%s\n与户主关系:%s\n性别:%s\n"(temp["name"],temp["irthday"],temp["home"],temp["race"],temp["relation"],temp["sex"]))
								break
				if flag ==0:
						print("查无此人")
				else:
						print("姓名:%s\n出生日期:%s\n籍贯:%s\n民族:%s\n与户主关系:%s\n性别:%s\n"%(cards[count-1]["name"],cards[count-1]["birthday"],cards[count-1]["home"],cards[count-1]["race"],cards[count-1]["relation"],cards[count-1]["sex"]))
		elif fun_number ==3:
				name = input("你输入要修改的名字")
				for temp in cards:
						if name == temp["name"]:
								print("1:修改名字".center(30," "))
								print("2:修改出生年月".center(30," "))
								print("3:修改籍贯".center(30," "))
								print("4:修改民族".center(30," "))
								print("5:修改与户主的关系".center(30," "))
								change_num = int(input("请选择修改序号"))
								if change_num ==1:
										name = input("请输入新的名字")
										temp["name"]=name
								elif change_num ==2:
										birthday=input("出生日期")
										temp["birthday"]=birthday
								elif change_num ==3:
										temp["home"]=input("籍贯")
								elif change_num ==4:
										temp["race"]=input("民族")
								elif change_num ==5:
										temp["relation"]=input("与户主关系")
								elif change_num ==6:
										temp["sex"]=input("性别")
								else:
									print("输入有误\n")
		elif fun_number ==4:
				name = input("请输入要删除的名字")
				flag =0#假设默认不存在
				for temp in cards:
						if name ==temp["name"]:
								flag = 1
								sure_num= int(input("确定要删除吗1:确定 2:返回"))
								if sure_num==1:
										cards.remove(temp)
										print("删除成功")
								break
				if flag ==0:
						print("没有此人")
		elif fun_number == 5:
					#二次确认
					break


