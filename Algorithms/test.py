"""Test."""
from random import shuffle

N = 200000
count = 0

for n in range(N):  # 1000次试验
    l = ['R'] * 30 + ['G'] * 10 + ['B'] * 20
    R = 30
    G = 10
    B = 20
    dic = {'R': R, 'G': G, 'B': B}
    shuffle(l)
    while dic['R']:
        a = l.pop()
        dic[a] -= 1
    if dic['G'] >= 1 and dic['B'] >= 2:
        count += 1

print(count/N)