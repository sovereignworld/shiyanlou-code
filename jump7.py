a = range(1,101)

for i in range(100):
	if a[i] % 7 == 0:
		continue
	elif a[i] % 10 == 7:
		continue
	elif a[i] // 10 == 7:
		continue
	print(a[i])
