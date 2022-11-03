import functools


# функция-декоратор должна принимать 1 аргумент и это будет не-вызванная функция (её имя без скобочек)
# внутри функции декоратора должна быть под-функция, которая будет вызываться
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")