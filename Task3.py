def myFunc(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0
a = [-1, -6, -7, 0, -8, 9, 10, 0, -18]
print('The original list:' + str(a))
res = map(myFunc, a)
nums = list(res)
print('The updated list:' + str(nums))