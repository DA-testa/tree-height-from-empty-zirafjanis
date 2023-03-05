import sys
import threading

def build_tree(n, parents):
    tree = {}
    root_index = 0
    
    for i in range(n):
        tree[i] = []
    
    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)
        else:
            root_index = i
            
    return tree, root_index


def compute_height(tree, root_index):
    queue = [(root_index, 1)]
    max_height = 0
    
    while queue:
        node, height = queue.pop(0)
        max_height = max(max_height, height)
        for child in tree[node]:
            queue.append((child, height+1))
            
    return max_height


def main():
    # Let the user input file name to use, don't allow file names with letter a
    # Account for github input imprecision
    letter = input()
    if "F" in letter:
        file_name = input()
        if "a" in file_name:
            return
        with open(f"./test/{file_name}", mode="r") as file:
            n = int(file.readline())
            parents = list(map(int, file.readline().split())) 
    elif "I" in letter:
        # Implement input from keyboard
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        return

    tree, root_index = build_tree(n, parents)
    print(compute_height(tree, root_index))


if __name__ == "__main__":
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
