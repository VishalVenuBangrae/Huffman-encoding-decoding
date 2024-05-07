from Huffman import *
import sys

def process_input(htree):
    plain1 = input("Plain Text: ")
    if plain1 == "q":
        return
    code = huffman_encoding(plain1, htree)
    print("Huffman(" + plain1 + ") = " + code)
    plain2 = huffman_decoding(code, htree)
    print("Decode(" + code + ") = " + plain2)
    process_input(htree)


def main():
    frequencies = freq(sys.argv[1])
    sorted_frequencies = sorted(frequencies, key=lambda x: x[1])
    initial_trees = list(map(lambda p: TreeNode(None, set(p[0]), p[1], None), sorted_frequencies))
    htree = construct_huffman_tree(initial_trees)
    pretty_print(htree, 0)
    process_input(htree)


main()
