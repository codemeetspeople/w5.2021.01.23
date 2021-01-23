def run_N_times(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)

        return wrapper
    return decorator


@run_N_times(5)
def hello(username):
    print(f'Hello, {username}!')


hello('caiman')
