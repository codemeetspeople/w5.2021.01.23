x = 1
y = 2
z = None  # initialize empty variable


if x > y:
    print(f'{x} > {y}')
else:
    print(f'{x} < {y}')


if x > 0:
    print(f'{x} is positive')
elif x % 2 == 0:
    print(f'{x} is even')
else:
    print(f'{x} is {x}')
