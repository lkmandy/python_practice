def distance(strand_a, strand_b):
    i = count = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("The Hamming distance cannot be measured for two DNA strands of different lengths")
    else:
        while i < len(strand_a) - 1:
            for a, b in strand_a, strand_a:
                if a == b:
                    count += 1
    return count
