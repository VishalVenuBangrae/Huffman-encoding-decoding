from TreeNode import *


def freq(fname):
    with open(fname, encoding='utf-8') as f:
        cont = f.read()
        store = {}
        for i in cont:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1
        final = []
        for j in store:
            final.append([j, store[j]])
        return final


def construct_initial_trees(sorted_frequencies):
    if len(sorted_frequencies) == 0:
        return []
    t = TreeNode(None, {sorted_frequencies[0][0]}, sorted_frequencies[0][1], None)
    return [t] + construct_initial_trees(sorted_frequencies[1:])


def combine(t1, t2):
    return TreeNode(t1, t1._symbols.union(t2._symbols), t1._weight + t2._weight, t2)


def insertHT(t, tlist):
    if tlist == []:
        return [t]
    if t._weight <= tlist[0]._weight:
        return [t] + tlist
    return [tlist[0]] + insertHT(t, tlist[1:])


def isort(tlist):
    if tlist == []:
        return []
    return insertHT(tlist[0], isort(tlist[1:]))


def construct_huffman_tree(tlist):
    if len(tlist) == 1:
        return tlist[0]
    j = combine(tlist[0], tlist[1])
    return construct_huffman_tree(insertHT(j, tlist[2:]))


def code(c, htree, present=""):
    if htree is None:
        return None

    if htree._left is None and htree._right is None:
        if str(htree._symbols)[2] == c:
            return present
        else:
            return None
    else:
        left_code = code(c, htree._left, present + "0")
        if left_code is not None:
            return left_code
        right_code = code(c, htree._right, present + "1")
        return right_code


def huffman_encoding(s, htree):
    encoded_result = ""
    for char in s:
        coded = code(char, htree)
        if coded is not None:
            encoded_result += coded
        else:
            return None
    return encoded_result


def huffman_decoding(s, htree):
    answer = ""
    record = htree
    while len(s) != 0:
        symbol, s = decoder_helper(s, record)
        if len(str(symbol)) > 1:
            answer += str(symbol)[2]
    return answer


def decoder_helper(s, htree):
    if htree._left is None and htree._right is None:
        return htree._symbols, s
    if len(s) == 0:
        return "", ""
    comp = int(s[0])
    s = s[1:]
    if comp == 0:
        return decoder_helper(s, htree._left)
    else:
        return decoder_helper(s, htree._right)


def pretty_print(htree, indent):
    if htree != None:
        spaces = ""
        for x in range(indent):
            spaces = " " + spaces
        print(spaces, htree._symbols, htree._weight)
        pretty_print(htree._left, indent + 2)
        pretty_print(htree._right, indent + 2)
