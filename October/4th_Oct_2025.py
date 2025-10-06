** start of main.py **

def classification(temp):
    if temp >= 30000:
        return "O"
    elif 10000 <= temp <= 29999:
        return "B"
    elif 7500 <= temp <= 9999:
        return "A"
    elif 6000 <= temp <= 7499:
        return "F"
    elif 5200 <= temp <= 5999:
        return "G"
    elif 3700 <= temp <= 5199:
        return "K"
    elif 0 <= temp <= 3699:
        return "M"

** end of main.py **
