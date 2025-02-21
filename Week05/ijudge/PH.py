"""PH"""
def main(a):
    """PH"""
    if 0 <= a < 7:
        ans = "acidic"
    elif 7 < a <= 14:
        ans = "akaline"
    elif a == 7:
        ans = "neutral"
    else:
        ans = "error"
    return ans
print(main(float(input())))
