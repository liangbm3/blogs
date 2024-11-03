---
title: Python多线程、多进程和协程
date: 2024-11-03 15:20:04
description: 在Python中，多线程、多进程和协程是处理并发任务的三种常用方式。它们各有优缺点，适合不同的场景。
tags: 
    - Python
    - 日常总结
top_img: /img/Python多线程、多进程和协程/cover.png
cover: /img/Python多线程、多进程和协程/cover.png
---

# 1. 前言

在Python中，多线程、多进程和协程是处理并发任务的三种常用方式。它们各有优缺点，适合不同的场景。

# 2. python多线程

使用`threading`模块，`threading`模块通过共享内存来实现多线程，所有线程共享一样的变量，适用于I/O密集型任务。

## 2.1. 一个线程的完整周期
1. 新建：新建一个线程对象
2. 就绪：调用start方法后，线程对象等待运行，什么时候开始取决于调度
3. 运行：线程处于运行状态
4. 阻塞：处于运行状态的线程被阻塞
5. 死亡：线程执行完毕或异常退出，线程对象销毁并释放内存

## 2.2. 一些使用实例
1. 直接使用Thread创建线程对象

    ```python
    from threading import Thread
    
    def print_numbers(range_start, range_end):
        for i in range(range_start, range_end):
            print(i)
            
    t1 = Thread(target=print_numbers, args=(1, 10))
    t2 = Thread(target=print_numbers, args=(11, 20))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    ```

2. 重写父类`threading.Thread`创建线程

    ```python
    import threading 
    
    #继承Thread并重写
    class myThread(threading.Thread):
        #重写构造函数
        def __init__(self,start_num,end_num):
            threading.Thread.__init__(self)
            self.start_num = start_num
            self.end_num = end_num
        #重写run函数
        def run(self):
            print(f"线程开始{self.name}")
            for i in range(self.start_num,self.end_num):
                print(i)
            print(f"线程结束{self.name}")
            
    thread1 = myThread(1,10)
    thread2 = myThread(11,20)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    ```

# 3. python多进程

使用`multiprocessing`模块，用法和`threading`类似。一些使用实例如下：

1. 直接使用`Process`创建进程对象

    ```python
    import multiprocessing
    
    def print_numbers(range_start, range_end):
        for i in range(range_start, range_end):
            print(i)
    
    if __name__ == '__main__':      
        p1 = multiprocessing.Process(target=print_numbers, args=(1, 100))
        p2 = multiprocessing.Process(target=print_numbers, args=(110, 200))
    
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    ```
2. 重写父类`multiprocessing.Process`

    ```python
    import multiprocessing
    
    #继承Thread类并重写
    class myProcess(multiprocessing.Process):
        #重写构造函数
        def __init__(self,start_num,end_num):
            multiprocessing.Process.__init__(self)
            self.start_num = start_num
            self.end_num = end_num
        #重写run函数
        def run(self):
            print(f"进程开始{self.name}")
            for i in range(self.start_num,self.end_num):
                print(i)
            print(f"进程结束{self.name}")
    if __name__ == '__main__':
        process1 = myProcess(1,100)
        process2 = myProcess(110,200)
        
        process1.start()
        process2.start()
        
        process1.join()
        process2.join()
    ```
# 3. python线程池和进程池
系统启动一个新线程的成本是比较高的，因为它涉及与操作系统的交互。在这种情形下，使用线程池可以很好地提升性能，尤其是当程序中需要创建大量生存期很短暂的线程时，更应该考虑使用线程池。

线程池在系统启动时即创建大量空闲的线程，程序只要将一个函数提交给线程池，线程池就会启动一个空闲的线程来执行它。当该函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变成空闲状态，等待执行下一个函数。

此外，使用线程池可以有效地控制系统中并发线程的数量。当系统中包含有大量的并发线程时，会导致系统性能急剧下降，甚至导致Python 解释器崩溃，而线程池的最大线程数参数可以控制系统中并发线程的数量不超过此数。

使用实例：
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def spider(page):
    time.sleep(page)
    print(f"crawl task{page} finished")
    return page

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as t:
        obj_list = []
        for page in range(1, 5):
            obj = t.submit(spider, page)
            obj_list.append(obj)

        for future in as_completed(obj_list):
            data = future.result()
            print(f"main: {data}")
```
程序将 `task` 函数提交（submit）给线程池后，`submit` 方法会返回一个 `Future` 对象，`Future` 类主要用于获取线程任务函数的返回值。由于线程任务会在新线程中以异步方式执行，因此，线程执行的函数相当于一个“将来完成”的任务，所以 Python 使用 `Future` 来代表。

# 4. 协程
协程（Coroutines）是一种特殊的软件构造，它允许程序在执行过程中暂停并恢复执行，而不会丢失当前的执行上下文。与线程和进程不同，协程在单个线程中运行，通过调度机制实现并发，降低了上下文切换的开销，提高了程序的执行效率。协程通常用于处理I/O密集型任务，如网络请求、文件读写等。

使用`asyncio`库来实现协程示例：
```python
import asyncio

async def task(num):
    print(f"Task {num} started")
    await asyncio.sleep(1)
    print(f"Task {num} completed")

async def main():
    tasks = [task(i) for i in range(3)]  # 创建多个任务
    await asyncio.gather(*tasks)  # 并行运行所有任务，并等待它们完成

if __name__ == "__main__":
    asyncio.run(main())  # 运行主函数

```