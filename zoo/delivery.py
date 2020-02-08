import os
import random
from string import ascii_lowercase

from .config import ZOO_PATH


PATTERN = (
    '\n@animal_in_zoo\n'
    'class {class_name}(Animal):\n'
    '    @classmethod\n'
    '    def speak(cls):\n'
    '        print(f\'{{cls.get_name()}} say "{sound}-{sound}"\')\n\n'
)

def delivery(animal):
    sound = ''.join(
        [random.choice(ascii_lowercase) for _ in range(4)]
    )
    class_name = animal.capitalize()

    target = PATTERN.format(class_name=class_name, sound=sound)

    path = os.path.join(ZOO_PATH, 'animals.py')

    with open(path, 'r') as source:
        source_code = source.read()

    source_code += target

    with open(path, 'w') as destination:
        destination.write(source_code)
