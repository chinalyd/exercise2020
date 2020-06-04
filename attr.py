#!/usr/bin/env python3

class Animal(object):
    def __init__(self, name ,gender):
        self.name = name
        self.gender = gender
    def __getattribute__(self, attr):
        print('Call self.__getattribute__, visit {} attribute'.format(attr))
        if attr in ('name', 'gender'):
            return object.__getattribute__(self, attr)
        else:
            print('Take it to object.__getattr__')
            return object.__getattr__(self, attr)
    def __getattr__(self, attr):
        print('Call self.__getattr__, visit {} attribute'.format(attr))
        if attr == 'age':
            return 3
        else:
            return 'not found that attribute'

if __name__ == '__main__':
    print('dog = Animal(\'Dog Trump\',\'M\')')
    dog = Animal('Dog Trump', 'M')
    print(dog.name)
    print(dog.gender)
    print(dog.age)
    print(dog.address)
