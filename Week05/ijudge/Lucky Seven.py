"""Lucky Seven"""
def main(a):
    """Lucky Seven"""
    if a[-1] == "7":
        ans = "Lucky!!!"
    else:
        ans = "No"
    return ans
print(main(input()))
