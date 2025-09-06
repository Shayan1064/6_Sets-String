set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

is_subset = all(elem in set2 for elem in set1)

print("Set1 is subset of Set2:", is_subset)
