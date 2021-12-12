from collections import defaultdict

graph = defaultdict(list)

def dfs(u):
    global total
    if u == 'end':
        total += 1
        
    visited[u] = True
    
    for v in graph[u]:
        if not visited[v] or v.isupper():
            dfs(v)
    
    visited[u] = False

for line in open("input.txt", 'r', encoding='utf-8'):
    u, v = line.strip().split('-')
    graph[u].append(v)
    graph[v].append(u)

visited = {i: False for i in graph.keys()}
visited['start'] = True

total = 0
dfs('start')

print(total)
       