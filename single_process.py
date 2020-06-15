#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

def io_task():
    #time.sleep强行挂起当前进程1秒钟
    #挂起，就是进程停滞，后续代码无法运行，cpu无法进行工作的状态
    #相当于进行了1秒钟IO操作
    #在这1秒钟内，CPU可能被运算器派往其他进程/线程中工作
    time.sleep(1)

def main():
    start_time = time.time()
    #循环IO操作5次
    for i in range(5):
        io_task()
    end_time = time.time()
    #打印运行耗时，保留2位小数
    print('程序运行耗时：{:.2f}s'.format(end_time - start_time))

if __name__ == '__main__':
    main()

