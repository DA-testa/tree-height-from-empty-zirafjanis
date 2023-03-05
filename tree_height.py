import sys
import threading


def compute_height(n, parents):
    # Create a list to store the heights of each node
    heights = [-1] * n

    def dfs(node):
        # If the height of this node has already been computed, return it
        if heights[node] != -1:
            return heights[node]

        # If this node has no children, its height is 1
        if not parents[node] in parents:
            heights[node] = 1
            return 1

        # Compute the height of each child and take the maximum
        max_height = 0
        for child in range(n):
            if parents[child] == node:
                child_height = dfs(child)
                max_height = max(max_height, child_height)

        # Store the height of this node and return it
        heights[node] = max_height + 1
        return heights[node]

    # Find the root of the tree
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
            break

    # Compute the height of the tree
    height = dfs(root)
    return height


def main():
    # Get the input from the user
    input_type = input("Choose input type: F for file, I for console input: ")
    if input_type == "F":
        input_file = input("Enter input file name: ")
        with open(input_file) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    else:
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parents: ").split()))

    # Compute the height of the tree and print it
    max_height = compute_height(n, parents)
    print(max_height)


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
