"""Bank Notes"""
def main(a):
    """Bank Notes"""
    contain = []
    contain.append(a // 800)
    a %= 800
    contain.append(a // 200)
    a %= 200
    contain.append(a // 150)
    a %= 150
    contain.append(a // 60)
    a %= 60
    contain.append(a // 10)
    a %= 10
    for i in contain:
        print(i)
main(int(input()))
