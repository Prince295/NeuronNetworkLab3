from functions import *
from objects import *


T.append( Tn )
B.append( get_b( Tn ) )
for i in range(len(x)):
    S = recognition_x(T,x[i],B)
    if S != 0:
        summ, c = comparition(T[S],x[i])
        print(summ)
        if summ>p:
            retraining(c,T, B, S)
        else:
            training(x[i],T,B)
    else:
        print(0)
        training(x[i],T,B)


for i in range(len(T)):
    print(T[i][0], T[i][1],T[i][2],T[i][3])
    print( T[i][4], T[i][5], T[i][6], T[i][7] )
    print( T[i][8], T[i][9], T[i][10], T[i][11] )
    print('')



