import sys
import threading


def compute_height(n, parents):
  tree = [[] for _ in range(n)]
  for i in range(n):
    if parents[i] != -1:
      tree[parents[i]].append(i)

  def dfs(node, depth):
    if not tree[node]:
      return depth
    max_depth = depth
    for child in tree[node]:
      child_depth = dfs(child, depth + 1)
      max_depth = max(max_depth, child_depth)
    return max_depth

  root = parents.index(-1)
  height = dfs(root, 0)
  return height


def main():
  n = int(input())
  parents = list(map(int, input().split()))
  print(compute_height(n, parents))


sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)  
threading.Thread(target=main).start()
