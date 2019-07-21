from collections import Counter, namedtuple
from functools import singledispatch
import heapq


FreqElem = namedtuple("FreqElem", ("freq", "elem"))


class BinTree:
    @singledispatch
    def __init__(self, elem=None):
        self.freq_elem = elem
        self.left = None
        self.right = None

    def __str__(self):
        result = [self.freq_elem]
        if self.left is not None:
            result.append(self.left)
        if self.right is not None:
            result.append(self.right)
        return " ".join(map(str, result))

    def __lt__(self, other):
        return self.freq_elem < other.freq_elem

    def get_code(self, freg_elem: FreqElem):
        result = ""
        if self.freq_elem and self.freq_elem.elem == freg_elem.elem:
            return result
        elif self.left and freg_elem.elem in self.left.freq_elem.elem:
            return "0" + self.left.get_code(freg_elem)
        else:
            return "1" + self.right.get_code(freg_elem)


class Haffman:
    @singledispatch
    def __init__(self, line):
        self.line = line
        self.counter = Counter(line)
        self._constract_heap()
        self._constract_tree()

    @__init__.register(dict)
    def __init__(self, code_dict):
        self.code_dict = code_dict

    def _constract_tree(self):
        tree = None
        for _ in range(len(self.heap) - 1):
            tree = BinTree()
            a = heapq.heappop(self.heap)
            b = heapq.heappop(self.heap)
            tree.left = a
            tree.right = b
            tree.freq_elem = FreqElem(a.freq_elem.freq + b.freq_elem.freq, a.freq_elem.elem + b.freq_elem.elem)
            heapq.heappush(self.heap, tree)
        if not tree:
            tree = BinTree()
            tree.left = heapq.heappop(self.heap)
        self.tree = tree

    def _constract_heap(self):
        self.heap = [BinTree(FreqElem(value, key)) for key, value in self.counter.items()]
        heapq.heapify(self.heap)

    def get_code(self):
        result = []
        for elem, freq in self.counter.items():
            result.append(f"{elem}: {self.tree.get_code(FreqElem(freq, elem))}")
        return "\n".join(result)

    def varcount(self):
        return len(self.counter)

    def encode(self, line=None):
        line = line if line is not None else self.line
        result = "".join(self.tree.get_code(FreqElem(self.counter[c], c)) for c in line)
        return result

    def decode(self, msg):
        current = ""
        result = ""
        for m in msg:
            current += m
            if current in self.code_dict:
                result += self.code_dict[current]
                current = ""
        return result

    @staticmethod
    def parse_code_dict(code_dict):
        listed = code_dict.split("\n")
        result = {}
        for code_pair in listed:
            letter, code = code_pair.split(": ")
            result[code] = letter
        return result


#def test_one_letter():
#    h = Haffman("a")
#    assert 1 == h.varcount()
#    assert "a: 0" == h.get_code()
#    msg = h.encode()
#    assert 1 == len(msg)
#    assert "0" == msg
#
#
#def test_aaaa():
#    h = Haffman("aaaa")
#    assert 1 == h.varcount()
#    assert "a: 0" == h.get_code()
#    msg = h.encode()
#    assert 4 == len(msg)
#    assert "0000" == msg
#
#
#def test():
#    h = Haffman("abacabad")
#    assert 4 == h.varcount()
#    assert "a: 0\nb: 10\nc: 110\nd: 111" == h.get_code()
#    msg = h.encode()
#    assert 14 == len(msg)
#    assert "01001100100111" == msg
#
#
#def test_the_same_freq():
#    h = Haffman("abba")
#    assert 2 == h.varcount()
#    assert "a: 0\nb: 1" == h.get_code()
#    msg = h.encode()
#    assert 4 == len(msg)
#    assert "0110" == msg
#
#
#def test_beep_boop_beer():
#    h = Haffman("beep boop beer!")
#    assert 7 == h.varcount()
#    assert "b: 00\ne: 10\np: 111\n : 010\no: 110\nr: 0111\n!: 0110" == h.get_code()
#    msg = h.encode()
#    assert 40 == len(msg)
#    assert "0010101110100011011011101000101001110110" == msg


def test_decode_zero():
    code_dict = "a: 0"
    d = Haffman.parse_code_dict(code_dict)
    assert {"0": "a"} == d
    h = Haffman(d)
    msg = h.decode("0")
    assert "a" == msg


def test_decode():
    code_dict = "a: 0\nb: 10\nc: 110\nd: 111"
    d = Haffman.parse_code_dict(code_dict)
    assert {"0": "a", "10": "b", "110": "c", "111": "d"} == d
    h = Haffman(d)
    msg = h.decode("01001100100111")
    assert "abacabad" == msg


if __name__ == '__main__':
    #line = input()
    #h = Haffman(line)
    #msg = h.encode()
    #print(h.varcount(), len(msg))
    #print(h.get_code())
    #print(msg)
    var_letters, code_len = map(int, input().split())
    code_dict = {}
    for _ in range(var_letters):
        letter, code = input().split(": ")
        code_dict[code] = letter
    h = Haffman(code_dict)
    print(h.decode(input()))
