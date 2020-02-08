# args -> positional arguments, e.g.: f(x, y, z)
# kwargs -> key-value arguments, e.g.: f(host='localhost')

def multiply(*args):
    result = args[0]

    for elem in args[1:]:
        result *= elem

    return result


def make_dsn(user='root', host='localhost', port=53, **kwargs):
    return f'{user}@{host}:{port}'


params = {
    'user': 'caiman',
    'host': 'upyachka.ru',
    'port': 1488,
    'password': 'Pukan2020'
}

def god_like_function(*args, **kwargs):

    import ipdb
    ipdb.set_trace()

    print(multiply(*args))
    print(make_dsn(**kwargs))


god_like_function(1, 2, 3, 4, 5, user='user2', host='ukr.net')

