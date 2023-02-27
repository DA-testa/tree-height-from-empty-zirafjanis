import sys
import threading
import numpy


def compute_height(n, parents):
    tree = [[] for _ in range(n)]
    root = None

    # build tree
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    # compute height
    stack = [(root, 0)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        for child in tree[node]:
            stack.append((child, depth + 1))

    return max_depth


def main():
    # read input
    n = int(input())
    parents = list(map(int, input().split()))

    # compute height
    max_height = compute_height(n, parents)

    # output result
    print(max_height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
