#!/usr/bin/env python3

class UserData(object):
    def __init__(self, idnum, name):
        self.idnum = idnum
        self.name = name


class NewUser(UserData):
    def __call__(self, *arg, **kwargs):
        return '{}\'s id is {}'.format(self.name, self.idnum)




if __name__ == '__main__':
    user = NewUser(101, 'Jack')
    user()
