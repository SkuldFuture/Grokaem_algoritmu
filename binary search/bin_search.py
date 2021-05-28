def binary_search(list, item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high)//2
		guess = list[mid]
		if guess == item:
			return mid
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None


my_list = [i*i for i in range(1, 51)]

print(binary_search(my_list, int(input('Какое число хотите найти? '))))
print(binary_search(my_list, int(input('Какое число хотите найти? '))))
