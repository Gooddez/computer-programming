"""Game"""
def main(a,b):
    """Game"""
    ans = a % 3 if a % 3 == b % 3 else "Error"
    return ans
print(main(int(input()),int(input())))
