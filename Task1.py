nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(filter(lambda x: x % 2 == 0, nums))
print(len(a))

nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(filter(lambda x: x % 2 != 0, nums))
print(len(a))