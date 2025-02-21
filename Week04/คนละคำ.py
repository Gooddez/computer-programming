"""คนละคำ"""
def worder(word):
    """คนละคำ"""
    f = word[::2]
    l = word[1::2]
    print(f"In: {f}")
    print(f"D: {l}")
worder(input().split())
