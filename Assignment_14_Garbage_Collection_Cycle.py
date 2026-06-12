import gc
import sys

# Enable automatic garbage collection
gc.enable()

class Node:
    def __init__(self, name):
        self.name = name
        self.link = None

    def __del__(self):
        print(f"{self.name} is being garbage collected")

# Create Node A and Node B
A = Node("Node A")
B = Node("Node B")

# Create circular references
A.link = B
B.link = A

# Check reference counts
print("Reference count of A:", sys.getrefcount(A))
print("Reference count of B:", sys.getrefcount(B))

# Store object IDs for investigation
a_id = id(A)
b_id = id(B)

# Delete references
del A
del B

print("\nVariables A and B deleted")
print("Objects still exist because of circular reference")

# Force garbage collection
unreachable = gc.collect()

print("\nGarbage Collector executed")
print("Unreachable objects collected:", unreachable)
