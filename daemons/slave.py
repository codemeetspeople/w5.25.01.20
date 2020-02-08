import os
import requests
from connection import get_connection
from time import sleep


ACTIONS = {}
URL = 'https://devclub.com'


def action(description):
    def method_wrapper(method):
        if method.__name__ not in ACTIONS:
            ACTIONS[method.__name__] = description
        return method

    return method_wrapper


class Slave:
    def __init__(self):
        self._id = os.getpid()
        self._connection = get_connection()
        self._name = f'{self.__class__.__name__.lower()}:{self._id}'
        self._action_key = f'action:{self._id}'

        self._connection.set(self._name, self._id)

    @action(f'Send request to {URL} for resource health check.')
    def ping(self):
        response = requests.get(URL)
        if response.status_code != 200:
            print(f'{URL} is not available!')
            return
        print(f'{URL} is available!')

    @action('Powerful amazing incredible research!')
    def calc(self):
        print(f'Research complete: 2 + 7 = 9')

    @action('Kill daemon. Just kill. No mercy.')
    def kill(self):
        self.clean()
        exit()

    def clean(self):
        self._connection.delete(self._action_key)
        self._connection.delete(self._name)

    def run(self):
        while True:
            try:
                action = self._connection.get(self._action_key)

                if not action:
                    sleep(1)
                    continue

                if not hasattr(self, action):
                    print(f'No such action! ({action})')
                    self._connection.delete(self._action_key)
                    continue

                getattr(self, action)()
                self._connection.delete(self._action_key)
            except Exception as e:
                self.clean()
                if not isinstance(e, KeyboardInterrupt):
                    print(f'{self._name} fails with Exception')
                break


if __name__ == '__main__':
    slave = Slave()

    try:
        slave.run()
    except KeyboardInterrupt:
        slave.clean()
        exit()
