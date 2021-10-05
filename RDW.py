## @file
## @brief Return / Data / Words virtual machine (FORTH)

import config
import os, sys

## Return stack
R = []

## Data stack
D = []

## Workds = vocabulary
W = {}

## nop ( -- ) do nothing
def nop(): pass
## halt ( n -- ) stop system with return code
def halt(): sys.exit(pop())

## push ( -- o ) push object
def push(o): D.append(o); return D
## pop ( o -- ) pop object
def pop(): return D.pop()
## top ( o -- o ) get top element w/o its remove
def top(): return D[-1]

## dup ( o -- o o ) duplicate top object
def dup(): return push(top())
## drop ( o -- ) remove top element
def drop(): pop(); return D
## swap ( o1 o2 -- o2 o1 ) swap two objects
def swap(): return push(D.pop(-2))
## over ( o1 o2 -- o1 o2 o1 ) dup inner object
def over(): return push(D[-2])

## . ( ... -- ) clear data stack
def dot(): D.clear(); return D

## compile to vocabulary
def compile(fn):
    if callable(fn): W[fn.__name__] = fn; return W
    raise TypeError(['compile', type(fn), fn])

## build default vocabulary
def init():
    compile(nop); compile(halt)
    compile(dup); compile(drop); compile(swap); compile(over)
    W['.'] = dot

## system init
if __name__ == '__main__':
    init()
    print(W)
