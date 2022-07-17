# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
import sys

def greater(a,b):
    if a in ["+","-"] and b in ["*","/"]:
        return True
    return False

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

allexpre=[]
while True:
    line = sys.stdin.readline()
    #allexpre.append(list(line.strip()))
    if line == '\n':
        break
    allexpre.append(list(line.strip()))
    #expre = list(line.strip())

for expre in allexpre:
    numlist = []
    oplist = []
    for t in expre:
        if t in "0123456789":
            numlist.append(int(t))
        else:
            if len(oplist) == 0 or greater(t,oplist[-1])==True:
                oplist.append(t)
            else:
                num1=numlist.pop()
                num2=numlist.pop()
                op=oplist.pop()
                r = doMath(op,num2,num1)
                numlist.append(r)
                oplist.append(t)

    while len(numlist)>1:
        num1 = numlist.pop()
        num2 = numlist.pop()
        op = oplist.pop()
        r = doMath(op, num2, num1)
        numlist.append(r)
    r = numlist[-1]
    print(int(r))


