#!/usr/bin/env python3

class UserData:
       
    def __init__(self, idnum, name):
        self.idnum = idnum
        self.name = name

    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.idnum, self.name)

if __name__ == '__main__':
    user1 = UserData(101, 'Jack')
    user2 = UserData(102, 'Louplus')
    print(user1)
    print(user2)
