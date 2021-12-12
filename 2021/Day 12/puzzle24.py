from collections import defaultdict

graph = defaultdict(list)

for line in open("input.txt", 'r', encoding='utf-8'):
    u, v = line.strip().split('-')
    graph[u].append(v)
    graph[v].append(u)

def dfs(u, b):
    global total
    if u == 'end':
        total += 1
        return
        
    visited[u] += 1
    
    for v in graph[u]:
        if v.isupper() or visited[v] == 0:
            dfs(v, b)
        # elif visited[v] == 0:
        #     dfs(v, b)
        elif visited[v] == 1 and not b:
            dfs(v, True)
    
    visited[u] -= 1

visited = {i: 0 for i in graph.keys()}
visited['start'] = True

total = 0
dfs('start', False)

print(total)
       