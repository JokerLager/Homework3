n = 0
zarab = input("""Твой заработок больше 1000 биткоинов в час
""")
if zarab == "да":
	n = n + 1
s = input("""Площадь твоего дома больше 1000 кв.м
""")
if s == "да":
	n = n + 1
h = input("""Расстояние от дна твоей машины до пола меньше 1 мм?
""")
if h == "да":
	n = n + 1
guest = input("""На свадьбе будет больше 1 000 000 гостей?
""")
if guest == "да":
	n = n + 1
if n == 4:
	print("""Поздравляю тебя ты стал моим женихом.""")
else:
	print("К сожалению ты не можешь быть моим женихом")