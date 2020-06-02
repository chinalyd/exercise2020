#!/usr/bin/env python3

class Animal(object):
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound \'I like eat Hamburder\' ')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + ' say \' Me either\' ')

class Monkey(Animal):
    def __init__(self, name, age=' '):
        super().__init__(name)
        self.age = age
    def make_sound(self):
        print(self.get_name() + ' say  \'I like Pizza\' ')

animals = [Dog('Dog Trump'), Cat('Cat Ivanka'), Monkey('Monkey Pence')]
for ani in animals:
    ani.make_sound()
