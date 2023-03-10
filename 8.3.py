import heapq
from collections import defaultdict

class HuffmanCoding:
    def __init__(self, message):
        self.message = message
        self.frequency = defaultdict(int)
        self.code_table = {}
        self.encoded_message = ''
        self.decoded_message = ''

    def create_frequency_dict(self):
        for char in self.message:
            self.frequency[char] += 1

    def create_huffman_tree(self):
        heap = [[freq, [char, ""]] for char, freq in self.frequency.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            for pair in left[1:]:
                pair[1] = '0' + pair[1]
            for pair in right[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
        self.huffman_tree = sorted(heapq.heappop(heap)[1:], key=lambda x: (len(x[-1]), x))

    def create_code_table(self):
        self.code_table = {char: code for char, code in self.huffman_tree}

    def encode(self):
        for char in self.message:
            self.encoded_message += self.code_table[char]

    def decode(self):
        inverted_code_table = {code: char for char, code in self.code_table.items()}
        code = ''
        for bit in self.encoded_message:
            code += bit
            if code in inverted_code_table:
                self.decoded_message += inverted_code_table[code]
                code = ''

    def print_tree(self):
        for char, code in self.huffman_tree:
            print(f"{char}: {code}")

    def run(self):
        self.create_frequency_dict()
        self.create_huffman_tree()
        self.create_code_table()
        self.encode()
        self.decode()
        print(f"Original message: {self.message}")
        print(f"Encoded message: {self.encoded_message}")
        print(f"Decoded message: {self.decoded_message}")
        print(f"Number of bits in encoded message: {len(self.encoded_message)}")
        print(f"Number of characters in original message: {len(self.message)}")
        if len(self.message) < 10:
            print("Huffman tree:")
            self.print_tree()

message = "abracadabra"
huffman = HuffmanCoding(message)
huffman.run()
