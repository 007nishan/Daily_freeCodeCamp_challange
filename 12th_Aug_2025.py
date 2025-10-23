** start of main.py **

def is_valid_number(n, base):
    #convert string to uppercase to make it case-sensitive
    n = n.upper()
    #create a string of valid digits for the given base
    valid_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base]
    ## Check EACH digit - only return True if ALL digits are valid
    for digit in n:
        if digit not in valid_digits:
            return False
    return True ## Return True only after checking all digits


** end of main.py **
