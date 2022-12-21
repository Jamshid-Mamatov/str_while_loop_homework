def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count=0
    i=0
    length=len(s)
    while length>i:
        if s[i].isalpha():
            count+=1
            print(s[i])    
        i+=1
    return count

print(main("Python 2022"))