from typing import List, Optional, Callable

class Node:
    def __init__(self, name, children: Optional[List['Node']] = None, evaluation_index: Optional[int] = None):
        self.name = name
        self.children = children if children is not None else []
        self.evaluation_index = evaluation_index

    def add_child(self, child_node: "Node"):
        if not isinstance(child_node, Node):
            raise TypeError(f"child_node must be a Node, got {type(child_node).__name__}")
        self.children.append(child_node)

    # def get_children(self) -> Union[List["Node"], None]:
    #     """Return the list of child Node objects or None if no children exist."""
    #     return list(self.children) if self.children else None
    def get_children(self) -> list:
        """Return the list of child Node objects."""
        return list(self.children)

    def get_children_names(self) -> list:
        """Return the list of child node names."""
        return [child.name for child in self.children]
    
    
    def traverse(self, inp, callback: Optional[Callable] = None):
        res = self.me.transform(inp)
        if self.evaluation_index is not None:
            if callback is None:
                raise RuntimeError("evaluation_index is set but no callback was provided")
            callback(res, self.evaluation_index)
        for child in self.children:
            child.traverse(res, callback)

    def __repr__(self):
        children_repr = ', '.join(repr(child) for child in self.children)
        return f"Node({self.name}, [{children_repr}])"

class DAG:
    def get_root_nodes(self) -> list:
        """Return a list of root nodes (nodes with no parents)."""
        all_children = set()
        for node in self.nodes.values():
            all_children.update(child.name for child in node.children)
        return [node for node in self.nodes.values() if node.name not in all_children]
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)
        return self.nodes[name]

    def add_edge(self, parent_name, child_name):
        parent = self.add_node(parent_name)
        child = self.add_node(child_name)
        parent.add_child(child)

    def get_children(self, parent_name: str) -> list:
        """Return the child Node objects for the node named parent_name.

        Raises KeyError if the parent node does not exist.
        """
        parent = self.nodes[parent_name]
        return parent.get_children()

    def get_children_names(self, parent_name: str) -> list:
        """Return the child node names for the node named parent_name.

        Raises KeyError if the parent node does not exist.
        """
        parent = self.nodes[parent_name]
        return parent.get_children_names()



# Create the DAG
dag = DAG()

# Add edges for the first component
dag.add_edge("AB", "C")
dag.add_edge("AB", "D")
dag.add_edge("C", "E")


# Print the list of root nodes (disconnected components)
print(dag.get_root_nodes())