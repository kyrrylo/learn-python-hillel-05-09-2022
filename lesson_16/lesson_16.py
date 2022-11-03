from decorators import count_calls
import functools


@count_calls
def say_hi(name):
    print(f'Hello, {name}')


# 1 1 2 3 5 8 13 21 34 55
@functools.lru_cache(maxsize=3)
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == '__main__':
    say_hi('Bob')
    say_hi('Rob')
    say_hi('Lee')
    say_hi('Hannah')

    print(fibonacci(10))
