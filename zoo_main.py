from zoo import animals
from zoo.delivery import delivery
from importlib import reload

while True:
    try:
        available = ', '.join(animals.ANIMALS.keys())
        print(f'available: {available}')
        print(f'Make your choice:')

        action = input().strip().lower()

        if action == 'exit':
            print('Bye-bye!')
            break

        if action in animals.ANIMALS:
            animals.ANIMALS[action].speak()
            print('+++ == +++')
            print()
            continue

        print(f'{action} is not available! Just a moment...')
        print('+++ == +++')
        print()
        delivery(action)
        reload(animals)
    except (KeyboardInterrupt, EOFError):
        print('Bye-bye!')
        break

