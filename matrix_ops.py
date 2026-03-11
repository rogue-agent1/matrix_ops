#!/usr/bin/env python3
"""Matrix operations."""
import sys
def show(m,name=''):
    if name: print(f"{name}:")
    for row in m: print(' '.join(f'{x:8.3f}' for x in row))
def mul(a,b):
    r=len(a); c=len(b[0]); n=len(b)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(c)] for i in range(r)]
def det(m):
    n=len(m)
    if n==1: return m[0][0]
    if n==2: return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    return sum((-1)**j*m[0][j]*det([r[:j]+r[j+1:] for r in m[1:]]) for j in range(n))
def transpose(m): return [list(r) for r in zip(*m)]
def inverse(m):
    n=len(m); aug=[r[:]+[1 if i==j else 0 for j in range(n)] for i,r in enumerate(m)]
    for i in range(n):
        mx=max(range(i,n),key=lambda r:abs(aug[r][i]))
        aug[i],aug[mx]=aug[mx],aug[i]
        if abs(aug[i][i])<1e-10: return None
        div=aug[i][i]; aug[i]=[x/div for x in aug[i]]
        for j in range(n):
            if j!=i: f=aug[j][i]; aug[j]=[aug[j][k]-f*aug[i][k] for k in range(2*n)]
    return [r[n:] for r in aug]
A=[[1,2,3],[4,5,6],[7,8,10]]
show(A,'A'); print(f"det(A) = {det(A):.3f}")
inv=inverse(A)
if inv: show(inv,'A⁻¹'); show(mul(A,inv),'A·A⁻¹')
