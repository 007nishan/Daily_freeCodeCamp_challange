** start of main.py **

def is_balanced(s):
    s1_vowel_count = 0
    s2_vowel_count = 0
    vowel = set('aeiou')
    if len(s)%2 == 0:
        s1 = s[:(len(s)//2)]
        s2 = s[(len(s)//2):]
    else:
        s1 = s[:(len(s)//2)]
        s2 = s[(len(s)//2)+1:]
    for i in s1.lower():
        if i in vowel:
            s1_vowel_count += 1
        else:
            continue
    for i in s2.lower():
        if i in vowel:
            s2_vowel_count += 1
        else:
            continue
    if s1_vowel_count == s2_vowel_count:
        return True
    else:
        return False

** end of main.py **
