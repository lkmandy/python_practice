def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The Hamming distance cannot be measured for two DNA strands of different lengths")
    else:
        compare = [a != b for a, b in zip(strand_a, strand_b) if a != b]
        result = sum(compare)
    return result
