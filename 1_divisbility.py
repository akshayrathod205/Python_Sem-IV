start_num = 2000
end_num = 3200
count = start_num
while count <= end_num:
	if count % 7 == 0 and not count % 5 == 0:
		print(count,'', sep = '-', end = '')
	count += 1
