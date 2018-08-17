import indiansnacksdataset as data

snacks = ['samosa ']
i = 0
for snack in snacks:
	train_data = data.load_train_data(snack,i)
	i = i + 1


#test_data = data.load_test_data()

