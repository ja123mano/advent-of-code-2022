def get_data():
    with open("Day 13\\input.txt", "r") as file:
        guide = list(map(str.splitlines, file.read().strip().split("\n\n")))
    return guide

def recursive_check(left, right):
    if type(left) == int:
        if type(right) == int:
            return left - right
        else:
            return recursive_check([left], right)
    else:
        if type(right) == int:
            return recursive_check(left, [right])
    
    for l, r in zip(left, right):
        val = recursive_check(l, r)
        if val:
            return val
    
    return len(left) - len(right)

def day_13_function(part="PartI"):
    
    if part == "PartI":
        packets = get_data()
        correct_packets = 0

        for i, (l_pack, r_pack) in enumerate(packets):
            if recursive_check(eval(l_pack), eval(r_pack)) < 0:
                correct_packets += i+1

        return correct_packets
    
    else:
        packets = list(map(eval, open("Day 13\\input.txt").read().split()))

        index_2 = 1
        index_6 = 2

        for packet in packets:
            if recursive_check(packet, [[2]]) < 0:
                index_2 += 1
                index_6 += 1
            elif recursive_check(packet, [[6]]) < 0:
                index_6 += 1
        
        return index_2 * index_6

if __name__ == "__main__":
    correct_packets = day_13_function()
    print(correct_packets)

    decoder_key = day_13_function("PartII")
    print(decoder_key)