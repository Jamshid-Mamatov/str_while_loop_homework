def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum=0
    i=0
    lenght=len(s)
    while lenght>i:
        if s[i].isdigit():
            sum+=int(s[i])

        i+=1
    return sum
