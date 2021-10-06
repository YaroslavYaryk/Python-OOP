import json

class Node:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

class Tree:

    def __init__(self):
        self.root = None 

    def insert(self, value):
        """insert value to the tree""" 

        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)


    def _insert(self, value, cur_node):

        if list(value.keys())[0] < list(cur_node.value.keys())[0]:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)

        elif list(value.keys())[0] > list(cur_node.value.keys())[0]:
            if cur_node.right is None:
                cur_node.right = Node(value)     
            else:
                self._insert(value, cur_node.right)

        else:
            print(f"Value({value}) already in tree")                             


    def search(self, value):
        """ find value in the tree """

        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False


    def _search(self, value, cur_node):

        if value == list(cur_node.value.keys())[0]:
            return cur_node.value
        elif value < list(cur_node.value.keys())[0] and cur_node.left is not None:
            return self._search(value, cur_node.left)
        elif value > list(cur_node.value.keys())[0] and cur_node.right is not None:
            return self._search(value, cur_node.right)
        else:
            return False


class BinaryTree:

    tree_storage = Tree()

    def __init__(self, cod, price): 
        if not (isinstance(cod, int) and isinstance(price, (int, float))):
            raise TypeError("kod and peice must be integers")
        BinaryTree.tree_storage.insert({cod:price})


    @classmethod
    def get_product(cls, product_code, quantity):
        return quantity * cls.tree_storage.search(product_code)[product_code]      


with open("product_list.json", "r") as file:
    for elem in json.load(file):
        BinaryTree(int(list(elem.keys())[0]), int(elem[list(elem.keys())[0]]))

def main():
    num = int(input("How many products? "))
    result = 0
    for i in range(num):
        product_code, quantity = map(int, input("code : quantity:  ").split(" : "))
        result += BinaryTree.get_product(product_code, quantity)
    return result    


print(f"Total price - {main()}$")   

