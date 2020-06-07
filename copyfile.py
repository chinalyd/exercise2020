#!/usr/bin/env python3

import sys

def copy_file(src, dst):
    with open(src, 'r') as src_file:
        with open(dst, 'w') as dst_file:
            #dst_file.write(src_file.read())
            list = src_file.readlines()
            for a, b in enumerate(list):
                if a == 0:
                    continue
                dst_file.write('{} {}'.format(a, b))


if __name__ == '__main__':
    file_a = '/home/shiyanlou/shiyanlou.txt'
    file_b = '/home/shiyanlou/shiyanlou_copy.txt'
    copy_file(file_a, file_b)
    #file = open(file_b)
    #list = file.readlines()
    #for a, b in enumerate(list):
        #print('{} {}'.format(a, b))

