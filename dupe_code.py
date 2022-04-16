import itertools

# Removes duplicates in the supercell coordinates
def duplicate(dupes):
    tmp = []
    for coord in dupes:
        if coord not in tmp:
            tmp.append(coord)
    return tmp
