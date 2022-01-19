def DFS(v):
    if v == n+1:
        for i in range(1, n):
            if ck[i] == 1:
                print(i, end = ' ')
        print()
    else:
        ck[v] = 1
        DFS(v+1)
        ck[v] = 0
        DFS(v+1)

n=4
ck = [0]*(n+1)
DFS(1)