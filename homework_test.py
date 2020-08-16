import pytest
from homework import Node, BST

n1 = Node(1)
n3 = Node(3)
n4 = Node(4)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n10 = Node(10)
n13 = Node(13)
n14 = Node(14)

n8.left = n3
n8.right = n10
n3.left = n1
n3.right = n6
n6.left = n4
n6.right = n7
n8.right = n10
n10.right = n14
n14.left = n13

@pytest.fixture
def bsttest():
    return BST(n8)   

@pytest.fixture
def emptytree():
    return BST()

def test_find_val():
    assert bsttest.find_val(8) == 8
    assert bsttest.find_val(3) == 3

def test_insert_val(val):
    bsttest.insert_val(17)
    assert bsttest.find_val(17) == n14.right

def test_print_tree():
    assert bsttest.print_tree != None