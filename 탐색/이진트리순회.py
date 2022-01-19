'''
이진트리 순회(깊이우선탐색,DFS)

왼쪽 자식노드 = 부모노드 * 2
오른쪽 자식노드 = 부모노드 * 2 + 1
'''

def DFS(v):
    if v > 7:
        return
    else:
        print(v, end = " ")     #중-왼-오 : 전위
        DFS(v*2)
        DFS(v*2 + 1)
             
        #DFS(v*2)                #왼-중-오 : 중위
        #print(v, end = " ")
        #DFS(v*2 + 1)
        
        #DFS(v*2)                #왼-오-중 : 후위
        #DFS(v*2 + 1)
        #print(v, end = " ")
    

DFS(1)