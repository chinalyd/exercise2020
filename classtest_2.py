#!/usr/bin/env python3

class UserData:
    def __init__(self, idnum, name):
        self.idnum = idnum
        self.name = name
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.idnum, self.name)

class NewUser(UserData):

    group = 'shiyanlou-louplus'

    def get_name(self):
        return self.name
    def set_name(self, value):
        self.name = value
    @classmethod
    def get_group(cls):
        return cls.group

    def __repr__(self):
        return '{}\'s id is {}'.format(self.name, self.idnum)
    
    @classmethod
    def format_userdata(cls, idnum, name):
        cls.idnum = idnum
        cls.name = name
        return '{}\'s id is {}'.format(cls.name, cls.idnum)

if __name__ == '__main__':
    print(NewUser.get_group())
    print(NewUser.format_userdata(109, 'Lucy'))

