def big_year(year):
	if (year%400==0) or(year%4==0 and year%100!=0):
		print("闰年")
	else:
		print("平年")
year = int(input("请输入一个年份"))
big_year(year)






