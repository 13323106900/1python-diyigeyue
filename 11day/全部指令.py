id_card = {"name":"小明","age":14,"sex":"女","group":"汉"}
print(id_card)

id_card["address"] = "山西"
id_card["merry"] ="单身"
#增
id_card["address"] = "北京市"
print(id_card)
#删
id_card.pop("sex")
print(id_card)
