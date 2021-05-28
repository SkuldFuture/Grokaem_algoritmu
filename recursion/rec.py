def factorial(i):
	if i == 1:
		return 1
	return i * factorial(i-1)


print(factorial(6))


def summer(a):
	if not a:
		return 0
	return a[0] + summer(a[1:])


print(summer([1, 2, 3, 4, 50]))


def count(b):
	if not b:
		return 0
	return 1 + count(b[1:])


print(count([1, 2, 3, 4, 5]))


def max(x):
	if len(x) == 2:
		return x[0] if x[0] > x[1] else x[1]
	sub_max = max(x[1:])
	return x[0] if x[0] > sub_max else sub_max


print(max([61, 2, 3, 41, 51]))
