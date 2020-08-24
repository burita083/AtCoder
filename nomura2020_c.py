def binary_tree(r = None):
    return [r, [], []]
 
def put_root(root, new_val):
    root[0] = new_val
 
def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root
 
def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root
 
def get_root(root):
    return root[0]
 
def get_left(root):
    return root[1]
 
def get_right(root):
    return root[2]

N = int(input())

A = list(map(int, input().split()))

count = 1
for x in range(10):
  count *= 2
  print(count)
