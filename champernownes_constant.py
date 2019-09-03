# Unsolved

champernowne_sequence = list(range(1, 100))

# FIXME
def d(n, sequence):
    index = 0

    for i in range(n):
        index += len(str(i))

    return sequence[index]
