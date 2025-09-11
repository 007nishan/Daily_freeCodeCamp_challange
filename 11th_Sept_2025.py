def array_diff(arr1, arr2):
    unique = []
    for item in arr1:
        if item not in arr2 and item not in unique:
            unique.append(item)
    for item in arr2:
        if item not in arr1 and item not in unique:
            unique.append(item)

    return sorted(unique)
