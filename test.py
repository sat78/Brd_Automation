import os
from graphviz import Digraph

# 👇 Add Graphviz bin path manually
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

dot = Digraph()
dot.node("A", "Start")
dot.node("B", "End")
dot.edge("A", "B")

dot.render("test_graph", format="png", cleanup=True)
print("Graph created successfully!")
