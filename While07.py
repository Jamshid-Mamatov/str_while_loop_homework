def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """

    count=0
    i=0
    lenght=len(s)
    while lenght>i:
        if s[i].isdigit():
            if int(s[i])%2==0:
                count+=1

        i+=1
    return count
