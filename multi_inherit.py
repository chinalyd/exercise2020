#!/usr/bin/env python3

class A:
    def __init__(self):
        self.name = 'Simon'
    def testA(self):
        print('----TestA----')

class B:
    def __init__(self):
        self.age = 8
    def testB(self):
        print('----TestB----')

class Person(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def testPerson(self):
        print('---testPerson----')


person = Person()
print(person.name)
print(person.age)
person.testA()
person.testB()
person.testPerson()

