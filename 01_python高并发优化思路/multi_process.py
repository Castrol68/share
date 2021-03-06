#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import time
import multiprocessing

# 定义全局变量Queue
QUEUE = multiprocessing.Manager().Queue()

def fibonacci(n):
    '''斐波拉数列'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def init_queue():
    '''初始化队列'''
    while not QUEUE.empty():
        QUEUE.get()
    for _index in range(10):
        QUEUE.put(_index)

def task():
    while not QUEUE.empty():
        try:
            data = QUEUE.get(block=True, timeout=1)
            print('work', data, 'start', end=' -> ')
            fibonacci(34)
            print('end')
        except Exception as ex:
            print(str(ex))

if __name__ == "__main__":
    print('单进程测试开始')
    init_queue()
    start_time = time.time()
    task()
    single_time = time.time() - start_time

    print('\n多进程测试开始')
    init_queue()
    start_time = time.time()
    number = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(number)
    for i in range(number):
        pool.apply_async(task)
    pool.close()
    pool.join()
    multi_time = time.time() - start_time

    print("单进程执行：", single_time)
    print("多进程执行：", multi_time)
