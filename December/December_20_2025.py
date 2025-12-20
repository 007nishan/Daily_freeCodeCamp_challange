** start of main.py **

def purge_most_frequent(arr):
    if not arr:
        return []
    
    # Manually count frequency of each element
    freq_count = {}
    for elem in arr:
        if elem in freq_count:
            freq_count[elem] += 1
        else:
            freq_count[elem] = 1
    
    # Find the maximum frequency
    max_freq = 0
    for count in freq_count.values():
        if count > max_freq:
            max_freq = count
    
    # Get all elements with maximum frequency
    most_frequent = set()
    for elem, count in freq_count.items():
        if count == max_freq:
            most_frequent.add(elem)
    
    # Filter out the most frequent elements while preserving order
    result = []
    for elem in arr:
        if elem not in most_frequent:
            result.append(elem)
    
    return result

** end of main.py **


