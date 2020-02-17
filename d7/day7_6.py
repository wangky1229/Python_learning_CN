def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main(nb=20):
    for val in fib(nb):
        print(val)


if __name__ == '__main__':
    main(10)