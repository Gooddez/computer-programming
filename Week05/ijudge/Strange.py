"""Strange"""
def main(a,b,c):
    """Strange"""
    l = [a,b,c]
    if a % 2:
        l.sort(reverse=True)
    else:
        l.sort()
    for i in l:
        print(i)
main(int(input()),int(input()),int(input()))
