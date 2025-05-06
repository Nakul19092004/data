import pandas as pd
from collections import defaultdict
from anytree import Node, RenderTree
# pip install anytree
# Step 1: Load data from Excel
df = pd.read_excel("C:/Users/nakul/Downloads/Apriori.xlsx")
t = df['List of item Ids'].dropna().apply(lambda x: x.strip().upper().split())
n = len(t)

# Step 2: Get the minimum support
ms = round(float(input("Min support %: ")) / 100 * n)
print(f"\nMin Supp: {ms}")

# Step 3: Count frequency of each item
ic = defaultdict(int)
for x in t:
    for i in x:
        ic[i] += 1

# Step 4: Filter items based on minimum support
ic = {k: v for k, v in ic.items() if v >= ms}

# Step 5: Sort items based on their frequency
def si(x):
    return sorted([i for i in x if i in ic], key=lambda y: (-ic[y], y))

# Step 6: Filter transactions based on sorted items
ot = [si(x) for x in t if si(x)]

# Step 7: Define the FP-Tree node class
class N:
    def __init__(self, i, c, p):
        self.i = i  # item
        self.c = c  # count
        self.p = p  # parent
        self.ch = {}  # children (for branching)
        self.l = None  # link to next node

# Step 8: Build the FP-Tree
def bft(tr):
    r = N(None, 0, None)
    h = defaultdict(list)
    for x in tr:
        c = r
        for i in x:
            if i in c.ch:
                c.ch[i].c += 1
            else:
                c.ch[i] = N(i, 1, c)
                h[i].append(c.ch[i])
            c = c.ch[i]
    return r

# Step 9: Create FP-Tree
r = bft(ot)

# Step 10: Function to recursively build the tree structure
def ba(n, p=None):
    m = f"{n.i} ({n.c})" if n.i else "Root"
    x = Node(m, p)
    for c in n.ch.values():
        ba(c, x)
    return x

# Step 11: Print FP-Tree
print("\nFP-Tree:")
tr = ba(r)
for p, _, d in RenderTree(tr):
    print(f"{p}{d.name}")
