"""Get A"""
def main(n):
    """Get A"""
    tophalf = n//2
    lenght = n*2-1
    letter = 'A'
    print(f'{letter:^{lenght}}')
    for i in range(1,tophalf):
        txt = letter+' '*((i*2)-1)+letter
        print(f'{txt:^{lenght}}')
    print(f'{letter*(((tophalf+1)*2)-1):^{lenght}}')
    for i in range(tophalf+1,n):
        txt = letter+' '*((i*2)-1)+letter
        print(f'{txt:^{lenght}}')
main(int(input()))
