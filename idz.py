#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создайте функцию, подсчитывающую сумму элементов
массива по следующему алгоритму: массив делится пополам,
подсчитываются и складываются суммы элементов в каждой
половине.
Сумма элементов в половине массива подсчитывается
по тому же алгоритму,
то есть снова путем деления пополам.
Деления происходят, пока в получившихся кусках массива не окажется
по одному элементу и вычисление суммы, соответственно, не станет
тривиальным.
"""

from math import fsum


def rec(mass):
    if len(mass) == 2:
        return fsum(mass)
    elif len(mass) == 3:
        return fsum(mass)
    else:
        n = len(mass) // 2
        a = mass[:n]
        b = mass[n:]
        return rec(a) + rec(b)


if __name__ == '__main__':

    print("Введите массив чисел: ")
    chisla = list(map(float, input().split()))
    print(rec(chisla))
