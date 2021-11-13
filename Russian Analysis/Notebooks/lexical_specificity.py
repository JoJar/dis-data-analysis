import math
import operator
from math import log,exp,factorial,log10,pi

def stirling(n):
    return n*log(n)-n +(0.5*log(2*3.141592*n))

# size of total corpus,size of subcorpus,number of occurences of one word in large, number of occurences in small corpus
def lexical_specificity(T,t,f,k):
    lim=400
    expvalue=f*t/(T*1.0)
    small=False
    if (expvalue<k):
        if (f>lim):
            arg1=stirling(f)
        else:
            arg1=log(factorial(int(f)))
        if (T-f>lim):
            arg2=stirling(T-f)
        else:
            arg2=log(factorial(int(T-f)))
        if (t>lim):
            arg3=stirling(t)
        else:
            arg3=log(factorial(int(t)))            
        if (T-t>lim):
            arg4=stirling(T-t)
        else:
            arg4=log(factorial(int(T-t)))
        if (T>lim):
            arg5=stirling(T)
        else:
            arg5=log(factorial(int(T)))
        if (k>lim):
            arg6=stirling(k)
        else:
            arg6=log(factorial(int(k)))
        if (f-k>lim):
            arg7=stirling(f-k)
        else:
            arg7=log(factorial(int(f-k)))
        if (t-k>lim):
            arg8=stirling(t-k)
        else:
            arg8=log(factorial(int(t-k)))
        if (T-f-t+k>lim):
            arg9=stirling(T-f-t+k)
        else:
            arg9=log(factorial(int(T-f-t+k)))

        prob=arg1+arg2+arg3+arg4-arg5-arg6-arg7-arg8-arg9
        first_prod=-log10(math.e)*prob
        
        if(prob<log(0.1)):
            small=True
            prob1=1.0
            prob=1.0
            while (prob1!=0.0 and (prob/prob1)<10000000 and k<=f):                
                prob2=(prob1*(f-k)*(t-k))/((k+1)*(T-f-t+k+1))
                prob=prob+prob2
                prob1=prob2
                k+=1
    if small:
        score=first_prod-log10(prob)
        return score
    else:
        return 0

#print (lexical_specificity(10000,500,20,6))


