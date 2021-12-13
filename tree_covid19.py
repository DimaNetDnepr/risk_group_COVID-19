def main():

	def get(text, variants):
		while True:
			cmd = input(text)
			match variants:
				case "int":
					try:
						return int(cmd)
					except:
						print("ERROR! Enter a number!")
				case dict(variants):
					if cmd in variants.keys():
						return variants[cmd]
					else:
						keys = list(variants.keys())
						print(f"ERROR! Enter any value from this {keys}")


	params = {
		"Age": get("Enter your Age: ", "int"),
		"Weight": get("Enter your Weight (yes/no): ", {"yes":True, "no":False}),
		"Pressure": get("Enter your Preshure (yes/no): ", {"yes":True, "no":False}),
		"Breath": get("Enter your Breath (yes/no): ", {"yes":True, "no":False}),
		"Shugar": get("Enter your Shugar (yes/no): ", {"yes":True, "no":False}),
		"Smoking": get("Enter your Bad_habits (yes/no): ", {"yes":True, "no":False}),
		"Kidnay": get("Enter your Kidnase (yes/no): ", {"yes":True, "no":False}),
		"Blood": get("Enter your Blood (yes/no): ", {"yes":True, "no":False})
	}
	
	if params["Age"] >= 60 or params["Weight"] or params["Pressure"] or params["Breath"] or params["Shugar"] or params["Bad_habids"] or params["Kidnay"] or params["Blood"]:
		print("You can get complications in case of corona-virus disease / Вы можете получить осложнения в случае заболевания короновирусной инфекции")
		count = 0
		if params["Age"] >= 60:
			count += 1
			print("You have some problem with your Age / Ваш возраст подвержен большей опасности в случае заболевания")
		array = list(params.keys())
		array.remove("Age")
		for key in array:
			if params[key]:
				count += 1
				print(f"You have some problem with / У вас проблемы с {key}. Please consult a doctor immediately / Пожалуйста, обратитесь к врачу")

		# В зависимости от количества факторов выделяем особую группу риска,
		# тем самым показывая кому стоит в первую очередь вакцинироваться
		match count:
			case 2:
				print("Так как сразу по двум параметрам у вас организм подвержен к осложнениям в случае заражении COVID-19")
			case 3:
				print("Так как сразу по трём параметрам у вас организм подвержен к осложнениям в случае заражении COVID-19")
			case 4:
				print("Настоятельно рекомендуем привиться от COVID-19. Вы находитесь тяжёлой группе риска, так как сразу по четырём параметрам у вас организм подвержен к осложнениям в случае заражения")
			case 5:
				print("Настоятельно рекомендуем привиться от COVID-19. Вы находитесь тяжёлой группе риска, так как сразу по пяти параметрам у вас организм подвержен к осложнениям в случае заражения")
			case 6:
				print("Как можно скорее предпримите меры по вакцинации в ближайшее время, по 6 пунктам Вы подвержены опасности от COVID-19")
			case 7:
				print("Вам срочно нужно сделать прививку от COVID-19! У вас найвысшая степень риска")
			case 8:
				print("Вам срочно нужно сделать прививку от COVID-19! У вас найвысшая степень риска, люди с такими факторами здоровья выживают в 2% случаев")
	else:
		print("Вы находитесь не в группе риска! Носите маски и проветривайте помещения")


if __name__ == '__main__':
	main()
	input()
