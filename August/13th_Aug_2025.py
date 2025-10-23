** start of main.py **

def fibonacci_sequence(start_sequence, length):
    # Return empty list if length is 0
    if length == 0:
        return []
    
    # Return first 1 or 2 numbers if length is 1 or 2
    if length <= 2:
        return start_sequence[:length]
    
    # Initialize result list with starting numbers
    result = list(start_sequence)
    
    # Add new numbers to the sequence
    for i in range(2, length):
        next_num = result[i-1] + result[i-2]
        result.append(next_num)
    
    return result

** end of main.py **
