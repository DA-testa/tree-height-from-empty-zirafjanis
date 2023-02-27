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
  input_type = input("F vai I : ")
  if input_type == "F":
    with open("input.txt"
              ) as f:  #teksta fails kkads, vai jalauj pasam rakstit nosaukumu
      n = int(f.readline())
      parents = list(map(int, f.readline().split()))
  elif input_type == "I":
    n = int(input())  #pirma rinda
    parents = list(map(int, input().split()))  #otra rinda
  else:
    print("kkas neiet")
    return

  print(compute_height(n, parents))


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()
