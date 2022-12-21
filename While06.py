def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    count=0
    i=0
    vowel='aeiou'
    lenght=len(s)
    while lenght>i:
        if s[i].isalpha()==True and s[i] not in vowel:
            count+=1
        i+=1
    return count
