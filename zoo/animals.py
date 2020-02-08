ANIMALS = {}

def animal_in_zoo(cls):
    if cls.get_name() not in ANIMALS:
        ANIMALS[cls.get_name()] = cls
    return cls


class Animal:
    @classmethod
    def get_name(cls):
        return cls.__name__.lower()

    @classmethod
    def speak(cls):
        raise NotImplementedError()

@animal_in_zoo
class Wolf(Animal):
    @classmethod
    def speak(cls):
        print(f'{cls.get_name()} say "wooo-wooo"')


@animal_in_zoo
class Beaver(Animal):
    @classmethod
    def speak(cls):
        print(f'{cls.get_name()} say "trtr-trtr"')


@animal_in_zoo
class Cat(Animal):
    @classmethod
    def speak(cls):
        print(f'{cls.get_name()} say "meow-meow"')

@animal_in_zoo
class Tiger(Animal):
    @classmethod
    def speak(cls):
        print(f'{cls.get_name()} say "ouxw-ouxw"')


@animal_in_zoo
class Fox(Animal):
    @classmethod
    def speak(cls):
        print(f'{cls.get_name()} say "hwmf-hwmf"')

