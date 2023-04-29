import graphviz

from BST import *
import tkinter as tk
import os
import webbrowser

os.environ["PATH"] += os.pathsep + 'C:/Users/agamm/Downloads/Graphviz/bin'


class BSTVisualizer:
    def __init__(self):
        self.bst = BST()
        self.window = tk.Tk()
        self.window.geometry("530x360")
        self.window.title("BST Visualizer")
        self.window.configure(relief="ridge", borderwidth=8, bg="#9192ff")
        self.window.grid_propagate(True)
        self.label = tk.Label(self.window, text="Enter a number:", font=("Arial", 12, "bold"),
                              relief="ridge", borderwidth=5)
        self.label.grid(row=0, column=0, sticky="nsew", pady=10, padx=15, columnspan=3)
        self.label.configure(background="#0089ff", width=30, height=2, fg="white")

        self.entry = tk.Entry(self.window)
        self.entry.grid(row=1, column=1, sticky="nsew")
        self.entry.configure(width=20, relief="ridge", borderwidth=5)

        self.insert_button = tk.Button(self.window, text="Insert", relief="ridge", command=self.insert_number,
                                       borderwidth=5, font=("Arial", 10, "bold"))
        self.insert_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.insert_button.configure(width=12, height=1, bg="#004dd8", fg="white")
        self.window.update()

        self.delete_button = tk.Button(self.window, text="Delete", relief="ridge", command=self.delete_number,
                                       borderwidth=5, font=("Arial", 10, "bold"))
        self.delete_button.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
        self.delete_button.configure(width=12, height=1, bg="#8a96ff", fg="white")
        self.window.update()

        self.search_button = tk.Button(self.window, text="Search", relief="ridge", command=self.search_number,
                                       borderwidth=5, font=("Arial", 10, "bold"))
        self.search_button.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        self.search_button.configure(width=12, height=1, bg="#006cf4", fg="white")
        self.window.update()

        self.print_inorder_button = tk.Button(self.window, text="Print Inorder", relief="ridge",
                                              command=self.print_inorder,
                                              borderwidth=5, font=("Arial", 10, "bold"))
        self.print_inorder_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.print_inorder_button.configure(width=12, height=1, fg="white", bg="#4d4d9c")
        self.window.update()

        self.print_preorder_button = tk.Button(self.window, text="Print Preorder", relief="ridge",
                                               command=self.print_preorder, borderwidth=5,
                                               font=("Arial", 10, "bold"))
        self.print_preorder_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.print_preorder_button.configure(width=12, height=1, fg="white", bg="#8879f0")
        self.window.update()

        self.print_postorder_button = tk.Button(self.window, text="Print Postorder", relief="ridge",
                                                command=self.print_postorder, borderwidth=5,
                                                font=("Arial", 10, "bold"))
        self.print_postorder_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.print_postorder_button.configure(width=12, height=1, fg="white", bg="#d1a9ff")
        self.window.update()

        self.clear_tree_button = tk.Button(self.window, text="Clear Tree", relief="ridge", command=self.clear_tree,
                                           borderwidth=5,
                                           font=("Arial", 10, "bold"))
        self.clear_tree_button.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        self.clear_tree_button.configure(bg="red", width=12, height=1, fg="white")
        self.window.update()

        self.draw_tree_button = tk.Button(self.window, text="Draw Tree", relief="ridge",
                                          command=self.draw_tree, borderwidth=5,
                                          font=("Arial", 10, "bold"))
        self.draw_tree_button.grid(row=3, column=2, sticky="nsew", padx=10, pady=10)
        self.draw_tree_button.configure(bg="#17c000", fg="white", width=12, height=1)
        self.window.update()

        self.label1 = tk.Label(self.window, text="Tree view:", relief="ridge", borderwidth=5,
                               font=("Arial", 10, "bold"))
        self.label1.grid(row=8, column=1, sticky="nsew")
        self.label1.configure(background="#0089ff", width=30, height=1, fg="white")
        self.window.update()

        self.tree_view = tk.Label(self.window, text="", relief="ridge", borderwidth=5)
        self.tree_view.grid(row=11, column=0, columnspan=3, sticky="nsew", padx=15, pady=10)
        self.tree_view.config(height=2, background="white")

        self.github_button = tk.Button(self.window, text="Github", command=self.open_project_page,
                                       relief="ridge", borderwidth=5,
                                       font=("Arial", 10, "bold"))
        self.github_button.configure(width=12, height=1, bg="#ffde24", fg="white")
        self.github_button.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

    def open_project_page(self):
        webbrowser.open('https://github.com/soberyoda')

    def insert_number(self):
        try:
            value = int(self.entry.get())
            self.bst.insert(value)
            self.update_tree_view()
        except ValueError:
            pass

    def delete_number(self):
        try:
            value = int(self.entry.get())
            self.bst.delete(value)
            self.update_tree_view()
        except ValueError:
            pass

    def search_number(self):
        try:
            value = int(self.entry.get())
            result = self.bst.search(value)
            # ABY WYŚWIETLIĆ ADRES ELEMENTU NALEŻY ZAKOMENTOWAĆ LINIE 121 ORAZ 122
            if result is not None:
                result = True
            self.tree_view.config(text=str(result))
        except ValueError:
            pass

    def inorder_traversal(self, node, traversal_list):
        if node:
            self.inorder_traversal(node.left, traversal_list)
            traversal_list.append(node.value)
            self.inorder_traversal(node.right, traversal_list)

    def print_inorder(self):
        traversal_list = []
        self.inorder_traversal(self.bst.root, traversal_list)
        tree = " -> ".join(str(val) for val in traversal_list)
        self.tree_view.config(text=tree)

    def preorder_traversal(self, node, traversal_list):
        if node:
            traversal_list.append(node.value)
            self.preorder_traversal(node.left, traversal_list)
            self.preorder_traversal(node.right, traversal_list)

    def print_preorder(self):
        traversal_list = []
        self.preorder_traversal(self.bst.root, traversal_list)
        tree = " -> ".join(str(val) for val in traversal_list)
        self.tree_view.config(text=tree)

    def postorder_traversal(self, node, traversal_list):
        if node:
            self.postorder_traversal(node.left, traversal_list)
            self.postorder_traversal(node.right, traversal_list)
            traversal_list.append(node.value)

    def print_postorder(self):
        traversal_list = []
        self.postorder_traversal(self.bst.root, traversal_list)
        tree = " -> ".join(str(val) for val in traversal_list)
        self.tree_view.config(text=tree)

    def clear_tree(self):
        self.bst.root = None
        self.tree_view.config(text="")

    def draw_tree(self):
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.bst.root)
        dot.render('tree.gv', view=True)

    def _add_nodes(self, dot, node):
        if node:
            dot.node(str(node.value))
            if node.left:
                dot.edge(str(node.value), str(node.left.value))
                self._add_nodes(dot, node.left)
            if node.right:
                dot.edge(str(node.value), str(node.right.value))
                self._add_nodes(dot, node.right)

    def update_tree_view(self):
        nodes = []

        def add_node(node):
            if node is None:
                return
            nodes.append(str(node.value))
            add_node(node.left)
            add_node(node.right)

        add_node(self.bst.root)
        tree = " -> ".join(nodes)
        self.tree_view.config(text=tree)

    def run(self):
        self.window.mainloop()
