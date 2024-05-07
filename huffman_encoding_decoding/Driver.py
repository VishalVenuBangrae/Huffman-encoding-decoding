import sys
from TreeNode import *
from Huffman import *


def main():
    frequencies = freq(sys.argv[1])
    # frequencies = [['A',8],['C',1],['B',3],['D',1],['E',1],['F',1],['G',1],['H',1]]
    sorted_frequencies = sorted(frequencies, key=lambda x: x[1])
    initial_trees = construct_initial_trees(sorted_frequencies)
    # initial_trees = list(map(lambda p: TreeNode(None,set(p[0]),p[1],None), sorted_frequencies))
    # print(initial_trees)
    htree = construct_huffman_tree(initial_trees)
    pretty_print(htree, 0)
    # code = huffman_encoding("Python is a fun language",htree)
    # cannot test this because it uses symbols outside the set;
    code = huffman_encoding("A", htree)
    print(code)
    code = huffman_encoding("B", htree)
    print(code)
    code = huffman_encoding("C", htree)
    print(code)
    code = huffman_encoding("D", htree)
    print(code)
    code = huffman_encoding("E", htree)
    print(code)
    code = huffman_encoding("F", htree)
    print(code)
    code = huffman_encoding("G", htree)
    print(code)
    code = huffman_encoding("H", htree)
    print(code)
    code = huffman_encoding("BADGE", htree)
    print(code)
    plain = huffman_decoding(code, htree)
    print(plain)


main()
