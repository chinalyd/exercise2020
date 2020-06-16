#!/usr/bin/env python3

import os, time, random
from multiprocessing import Pool

def task(name):
    print('Task {} start, process ID: {}'.format(name, os.getpid()))
    start = time.time()

    time.sleep(random.random() * 3)

    end = time.time()
    print('Task {} end, process ID: {}'.format(name, os.getpid()))

if __name__ == '__main__':
    print('The main process, ID: {}'.format(os.getpid()))
    print('--------------------------------')

    p = Pool(4) #child process pool

    for i in range(1, 6):
        p.apply_async(task, args=(i, ))

    p.close()
    print('Start run child process...')
    p.join()
    print('--------------------------------')
    print('All children process ran over, the main process run at now. Process ID: {}'.format(os.getpid()))

