list = [{"beijing":{"mianji":1290,"remkou" :123123},"shanghai":{"    mianji":12331,"renko u":123123}}]
for i in list:
	for j in i.keys():
			for k in i[j].keys():
					print(j,k,i[j][k])
