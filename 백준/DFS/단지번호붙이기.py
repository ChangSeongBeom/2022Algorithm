# https://www.acmicpc.net/problem/2667
import sys

N=int(sys.stdin.readline())
arrList=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

dx=[-1,0,1,0]
dy=[0,-1,0,1]

