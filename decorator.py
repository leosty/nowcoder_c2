#!/usr/bin/python
#  -*- coding: UTF-8 -*-


def log(level, *args, **kvargs):
    def inner(func):

        ''' 可变参数
        * args 无名字的参数
        ** 有名字参数 kv
        '''

        def wrapper(*args, **kvargs):
            print level, 'before calling', func.__name__
            print level, 'args', args, 'kvargs', kvargs
            func(*args, **kvargs)
            print level, 'end calling', func.__name__

        return wrapper
    return inner


@log(level='INFO')
def hello(name, age):
    print 'hello', name, age


if __name__ == '__main__':
    hello('rocket', age=13)  # =log(hello())
