"""Sequence 1"""
def main(n):
    """Sequence 1"""
    for i in range(n):
        stop = 0
        for j in range(n):
            if j >= i:
                print(j+1,end=" ")
            else:
                stop = j+1
        for j in range(stop):
            print(j+1,end=' ')
        print()
main(int(input()))
