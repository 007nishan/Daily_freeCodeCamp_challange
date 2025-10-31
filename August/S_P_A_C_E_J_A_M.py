** start of main.py **

def space_jam(s):
    # Remove all spaces and create new string
    new_s = ''
    non_space_chars = [c for c in s if c != ' ']  # Get all non-space characters
    
    for i, char in enumerate(non_space_chars):
        if char.isalpha():  # If character is alphabetical
            new_s += char.upper()  # Convert to uppercase
        else:
            new_s += char  # Keep non-alphabetical characters as is
        
        if i < len(non_space_chars) - 1:  # If not the last character
            new_s += '  '  # Add two spaces
    
    return new_s


** end of main.py **
