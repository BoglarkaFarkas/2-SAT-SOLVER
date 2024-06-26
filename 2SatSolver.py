#ZDROJ: https://www.geeksforgeeks.org/2-satisfiability-2-sat-problem/
from collections import defaultdict

MAX = 100000
adj = defaultdict(list)
adj_inv = defaultdict(list)
visited = [False] * (MAX + 1)
visited_inv = [False] * (MAX + 1)
s = []
scc = [0] * (MAX + 1)
counter = 1
variable1 = []
variable2 = []
def add_edges(a, b):
    adj[a].append(b)

def add_edges_inverse(a,b):
    adj_inv[b].append(a)

def dfs_first(u):
    if visited[u]:
        return
    visited[u] = True
    for i in range(len(adj[u])):
        dfs_first(adj[u][i])
    s.append(u)

def dfs_second(u):
    if visited_inv[u]:
        return
    visited_inv[u] = True
    for i in range(len(adj_inv[u])):
        dfs_second(adj_inv[u][i])
    scc[u] = counter


def is_2_satisfiable(n, m, a, b):
    global counter
    for i in range(m):
        if a[i] > 0 and b[i] > 0:
            add_edges(a[i] + n, b[i])
            add_edges_inverse(a[i] + n, b[i])
            add_edges(b[i] + n, a[i])
            add_edges_inverse(b[i] + n, a[i])
        elif a[i] > 0 and b[i] < 0:
            add_edges(a[i] + n, n - b[i])
            add_edges_inverse(a[i] + n, n - b[i])
            add_edges(-b[i], a[i])
            add_edges_inverse(-b[i], a[i])
        elif a[i] < 0 and b[i] > 0:
            add_edges(-a[i], b[i])
            add_edges_inverse(-a[i], b[i])
            add_edges(b[i] + n, n - a[i])
            add_edges_inverse(b[i] + n, n - a[i])
        else:
            add_edges(-a[i], n - b[i])
            add_edges_inverse(-a[i], n - b[i])
            add_edges(-b[i], n - a[i])
            add_edges_inverse(-b[i], n - a[i])

    for i in range(1, (2 * n) + 1):
        if not visited[i]:
            dfs_first(i)

    while s:
        number = s.pop()
        if not visited_inv[number]:
            dfs_second(number)
            counter += 1

    for i in range(1, n+1):
        if scc[i] == scc[i+n]:
            print("NESPLNITELNA")
            return

    print("SPLNITELNA")
    for i in range(1, n+1):
        if scc[i] < scc[i+n]:
            print(f'x{i}: NEPRAVDA')
        else:
            print(f'x{i}: PRAVDA')
    return

def read_input(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().split()
        nbvar = int(first_line[0])
        nbclauses = int(first_line[1])

        for line in file:
            variable1.append(int(line.split()[0]))
            variable2Hodnota = int(line.split()[1])
            if variable2Hodnota == 0:
                variable2.append(int(line.split()[0]))
            else:
                variable2.append(variable2Hodnota)
        return nbvar,nbclauses
def main():
    filename = "inputexample.txt"
    nbvar,nbclauses = read_input(filename)
    is_2_satisfiable(nbvar, nbclauses, variable1, variable2)

if __name__ == "__main__":
    main()