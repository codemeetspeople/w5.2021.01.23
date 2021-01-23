from functools import reduce


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def sum2(x:int, y:int) -> int:
#     return x + y


# def mult(x, y):
#     # (int, int) => int
#     return x * y


# def wrapper(func, sequence):
#     result = sequence[0]

#     for elem in sequence[1:]:
#         result = func(result, elem)

#     return result


# print(lst)
# print(wrapper(sum2, lst))
# print(wrapper(mult, lst))
# print()

# print(lst)
# print(reduce(sum2, lst))
# print(reduce(mult, lst))
# print()

print(lst)
print(reduce(lambda x, y: x + y, lst))
print(reduce(lambda x, y: x * y, lst))
print()
