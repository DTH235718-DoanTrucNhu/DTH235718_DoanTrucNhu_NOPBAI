import math
import os
import sys

import module1
import module2

def add(a,b):
    return a+b
print(add(4,5))

print('Hello World!')

print('Albert Einstein đã từng nói: Một người không bao giờ mắc' \
' sai lầm không bao giờ thử bất kỳ điều gì mới.')

if 5>2:
    print('Five is greater than two!')

total = 1 + \
2 + \
33
print(total); print('Hello Python!')

if True:
    print('True')
else:
    print('False')

#This is a comment
print('Hello, World!')

if len(sys.argv) >=4:
    print("Tham so 1: ",sys.argv[1])
    print("Tham so 2: ",sys.argv[2])
    print("Tham so 3: ",sys.argv[3])
else:
    print("Vui lòng truyền đủ 3 tham số khi chạy chương trình.")
# python baitap1.py 1 2 3 

print(module1.question)
print(module2.question)
print(module1.answer)
print(module2.answer)

#baitap4 chuong 1
print('Chao cac ban!')

#baitap 5 chương 1
print('Lê Thị Yến Nhi')

#baitap 6 chương 1

print('Mình về mình có nhớ ta?')
print('Mười lăm năm áy thiết tha mặn nồng.')
print('Mình về mình có nhớ không?')
print('Nhìn cây nhớ núi, nhìn sông nhớ nguồn.')

#baitap 7 chương 1
if len(sys.argv) >= 2:
    print("Chuỗi nhập từ tham số:", sys.argv[1])
else:
    print("Vui lòng nhập chuỗi làm tham số khi chạy chương trình.")

#baitap 8 chương 1

width = 4   # chiều ngang
height = 6  # chiều dọc

for i in range(height):
    for j in range(width):
        # nếu là dòng đầu, dòng cuối, hoặc cột đầu, cột cuối -> in '*'
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#bai tap 9 chương 1
width = 9
height = 4

for _ in range(height):
    print('*' * width)

#bai tap 10 chương 1
h = [1, 3, 5, 3, 7, 9]   
max_width = max(h)      
for sao in h:
    space = (max_width - sao) // 2   
    print(" " * space + "*" * sao)
for _ in range(2):
    space = (max_width - 3) // 2
    print(" " * space + "*" * 3)

