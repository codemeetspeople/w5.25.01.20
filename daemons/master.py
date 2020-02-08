from connection import get_connection
from slave import ACTIONS
from time import sleep


class Master:
    def __init__(self):
        self._connection = get_connection()


    def daemons_list(self):
        daemons = self._connection.keys('slave:*')
        return daemons

    def actions_list(self):
        out = ''
        for action, description in ACTIONS.items():
            out += f'{action}: {description}\n'
        return out

    def notify_slave(self, slave, action):
        slave_elems = slave.split(':')
        slave = 'action:'+slave_elems[1]

        self._connection.set(slave, action, ex=5)

    def run(self):
        while True:
            try:
                daemons_list = self.daemons_list()
                if not daemons_list:
                    print('No available slaves')
                    sleep(10)
                    continue

                daemons = '\n'.join(daemons_list)
                print(f'{daemons}\n\n{self.actions_list()}')

                slave, action = input().strip().split(' ')

                if slave == 'all':
                    for sl in daemons_list:
                        self.notify_slave(sl, action)
                    continue

                self.notify_slave(slave, action)
            except Exception as e:
                print(e)
                break


if __name__ == '__main__':
    master = Master()

    try:
        master.run()
    except KeyboardInterrupt:
        exit()