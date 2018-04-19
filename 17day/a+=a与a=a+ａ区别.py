#对于可变数值来说，有差别，对于不可变数值来说，无差别
def sum(a,b):
	c=a+b
	print(c)


def sum1(a,b,*args,**kwargs):
	all_sum=0
	c=a+b
	all_sum+=c
	for i in args: 
		all_sum+=i
	for i in kwargs.values():
		all_sum+=i
	print(all_sum)

sum(1,2)
t=(1,2)
b={"age":12}
sum1(1,2,*t,**b)



