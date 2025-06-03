from itertools import chain

lists = [[1, 2], [3, 4], [5]]
flat_map= chain.from_iterable(map(lambda x: x, lists))
print(list(flat_map))


lists = [[1, 2], [3, 4], [5]]
flat = [item for sublist in lists for item in sublist]
print(flat)  

