from advent import Advent
import math

advent = Advent(2021, 16)

signal_bin = ''.join([bin(int(c, 16))[2:].zfill(4) for c in advent.lines[0]])
bit_i = 0

class Packet():
    literal = -1
    length_type = -1
    sub_packets = []

    def __init__(self, v, t):
        self.version = int(v, 2)
        self.type = int(t, 2)

    def is_literal(self):
        return self.type == 4

    def set_literal(self, literal):
        self.literal = int(literal, 2)

    def set_length_type(self, l):
        self.length_type = int(l, 2)
    
    def is_operator(self):
        return not self.is_literal()

    def get_op(self):
        if self.is_literal(): return self.literal
        if self.type == 0:
            return sum([pck.get_op() for pck in self.sub_packets])
        elif self.type == 1:
            return math.prod([pck.get_op() for pck in self.sub_packets])
        elif self.type == 2:
            return min([pck.get_op() for pck in self.sub_packets])
        elif self.type == 3:
            return max([pck.get_op() for pck in self.sub_packets])
        elif self.type == 5:
            return 1 if self.sub_packets[0].get_op() > self.sub_packets[1].get_op() else 0
        elif self.type == 6:
            return 1 if self.sub_packets[0].get_op() < self.sub_packets[1].get_op() else 0
        elif self.type == 7:
            return 1 if self.sub_packets[0].get_op() == self.sub_packets[1].get_op() else 0

    def __str__(self):
        s = 'Version: {}. Type: {}.'.format(self.version, self.type)
        if self.is_literal():
            s += ' Literal: {}'.format(self.literal)
        else:
            s += ' Length Type ID: {}. Subpackets: {}'.format(self.length_type, len(self.sub_packets))
        return s

def _parse_literal(packet):
    global bit_i
    literal, last_group = '', False
    while not last_group:
        last_group = not bool(int(signal_bin[bit_i]))
        literal += signal_bin[bit_i + 1 : bit_i + 5]
        bit_i += 5
    packet.set_literal(literal)

def _parse_operator(packet):
    global bit_i
    packet.set_length_type(signal_bin[bit_i])
    bit_i += 1
    if packet.length_type == 0:
        subpacket_bits = int(signal_bin[bit_i:bit_i+15], 2)
        bit_i += 15
        packet.sub_packets = parse_packets(max_idx=subpacket_bits+bit_i)
        # bit_i += subpacket_bits
    elif packet.length_type == 1:
        num_subpackets = int(signal_bin[bit_i:bit_i+11],2)
        bit_i += 11
        packet.sub_packets = parse_packets(max_packets=num_subpackets)


def parse_packets(max_packets=float('inf'), max_idx=len(signal_bin)):
    global bit_i
    packets = []
    curr_packet = None
    while bit_i < max_idx and len(packets) < max_packets:
        if not curr_packet:
            if int(signal_bin[bit_i:]) != 0:
                curr_packet = Packet(signal_bin[bit_i : bit_i + 3], signal_bin[bit_i + 3 : bit_i + 6])
            bit_i += 6
        else:
            if curr_packet.is_literal():
                _parse_literal(curr_packet)
            elif curr_packet.is_operator():
                _parse_operator(curr_packet)
            packets.append(curr_packet)
            curr_packet = None
        
    return packets

all_packets = parse_packets()

# Part 1
all_versions = 0
def sum_sub_packet_version(pck):
    global all_versions
    all_versions += pck.version
    for subpacket in pck.sub_packets:
        sum_sub_packet_version(subpacket)

sum_sub_packet_version(all_packets[0])

print(all_versions)

# Part 2
print(all_packets[0].get_op())