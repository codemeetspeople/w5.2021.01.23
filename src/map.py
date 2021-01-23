lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def increment(x):
#     return x + 1


# def pow2(x):
#     return x ** 2


# def wrapper(func, sequence):
#     result = []

#     for elem in sequence:
#         result.append(func(elem))

#     return result


# print(lst)
# print(wrapper(increment, lst))
# print(wrapper(pow2, lst))
# print()

# print(lst)
# print(list(map(increment, lst)))
# print(list(map(pow2, lst)))
# print()

print(lst)
print(list(map(lambda x: x + 1, lst)))
print(list(map(lambda x: x ** 2, lst)))
print()
