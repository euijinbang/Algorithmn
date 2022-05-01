from itertools import permutations, combinations

l = [1, 2, 3]
perm = list(map(list, permutations(l, 2)))
perm2 = list(map(list, permutations(l)))
comb = list(map(list, combinations(l, 2)))

