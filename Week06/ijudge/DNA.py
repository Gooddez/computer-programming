"""DNA"""
def main(n1,n2):
    """DNA"""
    a = True
    for ch in n1+n2:
        if ch not in ('ACGT'):
            a = False
            break
    if a:
        dnaCon = []
        for i in range(len(n1)):
            prev = None
            for j in range(i,len(n1)):
                j+=1
                if n1[i:j] in n2:
                    if n1[i:j]:
                        prev=n1[i:j]
                        dnaCon.append(prev)
                else:
                    dnaCon.append(prev)
                    break
        dnaCon = [x for x in dnaCon if x is not None]
        if dnaCon:
            index = list(map(len,dnaCon)).index(max(list(map(len,dnaCon))))
            ans = dnaCon[index]
        else:
            ans = None
    else:
        ans = "Error"
    return ans
print(main(input(),input()))
