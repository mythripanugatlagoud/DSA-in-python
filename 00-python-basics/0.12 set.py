set = {1,2,3,5,6}
def find_missing_number(set):
    for i in range(1,6):
        if i not in set:
            return i 
print(find_missing_number(set))
# find all pairs in a setwith a given difference
def find_pairs_with_difference(set, difference):
    pairs = []
    for num in set:
        if (num + difference) in set:
            pairs.append((num, num + difference))
    return pairs
print(find_pairs_with_difference({1,2,3,4,5}, 2))

