import numpy as np
from objects import *

def recognition_x(T,x,B):
    S=[]
    for i in range(len(T)):
        S.append(get_s(T[i],x,B[i]))
    return S.index(np.max(S))




def get_s(T,x,B):
    S = 0
    for i in range(len(x)):
        S += (T[i]&x[i])*B[i]
    return S

def training(x,T,B):
    T.append(x)
    B.append(get_b(x))
    return T, B


def get_b(x):
    b=0
    b_array = []
    b = (L) / (L - 1 + np.sum(x))
    for i in range(len(x)):
        b_array.append(b*x[i])
    return  b_array

def comparition(T, x):
    c=[]
    summ=0
    for i in range(len(T)):
        c.append(T[i] & x[i])
    for i in range(len(c)):
        if c[i]==x[i]:
            summ+=1
    summ=summ/len(x)
    return summ,c

def retraining(c,T, B, S):
    B[S] = get_b(c)
    T[S] = c
    return


def get_menu():
    i = input_number()

def input_number():
    while True:
        y = input( "Введите целое число" )
        try:
            y = int( y )
        except ValueError:
            print( "Это не целое число. Пожалуйста, введите число" )
            continue
        return y
        for i in range(len(x)):
            if y == i:
                return y
                break
            else:
                print("Введите число, соотвествующее номеру варианта")

def input_matrix_number():
    while True:
        y = input( "Введите 0 или 1" )
        try:
            y = int( y )
        except ValueError:
            print( "Это не 0 или 1" )
            continue
        return y
        for i in range(2):
            if y == i:
                return y
                break
            else:
                print("Введите 0 или 1")


def input_matrix():
    new_value = []
    for i in range(12):
        new_value[i] = input_matrix_number()
    x[input_number()] = new_value
    return x





