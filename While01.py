def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count=0
    length=len(s)
    i=0
    while length>i:
        if s[i].isdigit():
            count+=1
        i+=1
    return count
