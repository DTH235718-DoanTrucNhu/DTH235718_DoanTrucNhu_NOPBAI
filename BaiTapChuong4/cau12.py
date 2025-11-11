def oscillate(start, limit):
    # đi từ start đến 0
    for i in range(start, 1):
        yield i
        yield -i
    # 0 hai lần
    yield 0
    yield 0
    # đi lên tới limit-1
    for i in range(1, limit):
        yield i
        yield -i
for n in oscillate(-3, 5):
    print(n, end=' ')
print()
