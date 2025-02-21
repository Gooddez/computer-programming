"""Paper"""
def paper(s1,s2) :
    """paper"""
    if s1 == s2:
        print(1)
    else:
        first = int(s1[1:])
        last = int(s2[1:])
        print(2**(last-first))
paper(input(),input())
