from solucao import astar_hamming, astar_manhattan, astar_new_heuristic, bfs, dfs

estado = "2_3541687"

print("A* Hamming")
res = astar_hamming(estado)
print("Solução encontrada:", res)

print("\nA* Manhattan")
res = astar_manhattan(estado)
print("Solução encontrada:", res)

print("\nA* Heurística nova")
res = astar_new_heuristic(estado)
print("Solução encontrada:", res)

print("\nBFS")
res = bfs(estado)
print("Solução encontrada:", res)

print("\nDFS")
res = dfs(estado)
print("Solução encontrada:", res)

