import sys
import threading

def compute_height(n, parents):
    nodes = {}
    for i in range(n):
        nodes[i] = []

    for i in range(n):
        if parents[i] != -1:
            nodes[parents[i]].append(i)

    def dfs(node):
        heights = []
        for child in nodes[node]:
            heights.append(dfs(child))
        return max(heights) + 1 if heights else 1

    root = parents.index(-1)
    height = dfs(root)
    return height


def main():
    input_type = input("Choose input type: F for file, I for console input: ")
    if input_type == "F":
        input_file = input("Enter input file name: ")
        with open(input_file) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    else:
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parents: ").split()))

    max_height = compute_height(n, parents)
    print(max_height)


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
