import sys
input=lambda:sys.stdin.readline().strip()

def I():
    return input()

def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from collections import *
for _ in range(int(input())):
  t=int(input());b=max(Counter(input().split()).values());s=t-b
  while t>b:s+=1;b*=2
  print(s)


