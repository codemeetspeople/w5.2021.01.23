def my_range(start, end=None, step=None):
    if not end:
        start, end = 0, start

    if not step:
        step = 1

    while start < end:
        yield start

        start += step


if __name__ == '__main__':
    for i in my_range(4):
        print(i)

    for i in my_range(2, 5):
        print(i)

    # for i in my_range(1, 7, 2):
    #     print(i)
