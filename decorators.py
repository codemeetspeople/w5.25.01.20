DECORATED = {}


def run_N_times(times=10):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return inner_wrapper
    return wrapper


def add_decorated(func):
    if func.__name__ not in DECORATED:
        DECORATED[func.__name__] = run_N_times()(func)
    return func


@add_decorated
def machine(coffee_type='espresso', **kwargs):
    print(f'{coffee_type} maker...')


@add_decorated
def translate(f='ukrainian', t='french'):
    print(f'translate: {f}=>{t}')


@run_N_times(5)
def hello(user='caiman'):
    print(f'Hello, {user}!')


print('original function:')
machine()
print('========')
print()
print('decorated function:')
DECORATED[machine.__name__]()
