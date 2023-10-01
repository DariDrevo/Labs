def pascal(n):
    rows = [[1]]
    for i in range(2, n + 1):
        rows.append([1])
        while len(rows[i - 1]) != i - 1:
            next = rows[i - 2][len(rows[i - 1]) - 1] + rows[i - 2][len(rows[i - 1])]
            rows[i - 1].append(next)
        rows[i - 1].append(1)
    return rows


def use_pascal():
    n = int(input())
    rows = pascal(n)
    max_len = len(' '.join([str(i) for i in rows[-1]]))
    for row in rows:
        s = ' '.join([str(i) for i in row])
        print(' ' * ((max_len - len(s)) // 2) + s)

def draw_serpinski():
    n = int(input())
    pasc = pascal(2**n)
    rows = []
    for i in range(len(pasc)):
        rows.append([])
    for i in range(len(pasc)):
        for j in pasc[i]:
            rows[i].append(' ' if j % 2 == 0 else '*')
    max_len = len(' '.join(rows[-1]))
    for row in rows:
        s = ' '.join(row)
        print(' ' * ((max_len - len(s)) // 2) + s)

draw_serpinski()