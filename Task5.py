def rotate(l, n):
    return l[-n:] + l[:-n]
example_list = [1, 2, 3, 4, 5]

a = rotate(example_list, -1)
print("Negative rotation by 1:" + str(a))

b = rotate(example_list, 1)
print('Positive rotation by 1:' + str(b))
