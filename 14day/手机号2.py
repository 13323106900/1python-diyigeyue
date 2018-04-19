def check_pjone(phone):
	if phone.starswith("1") and len(phone)==11:
		return True
	else:
		return False

phone = input("请输入手机号")
result =check_phone(phone)
if result == False:
	print("手机号是错的")

phone2 = input("请输入手机号")
result = check_phone(phone2)
if result == False:
	print("手机号是错的")

