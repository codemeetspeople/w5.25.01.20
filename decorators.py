def run_N_times(times):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@run_N_times(5)
def hello(user):
    print(f'hello, {user}!')

@run_N_times(3)
def love_is(male, female):
    print(f'{male} + {female} = love')

@run_N_times(6)
def get_status(male, female, status='married'):
    print(f'{male} + {female} is {status}')

hello('caiman')
love_is('jonh', 'jane')
get_status('jonh', 'jane', status='gone away')
