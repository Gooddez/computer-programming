"""Sequence 2"""
def main(n):
    """Sequence 2"""
    txt = ''
    m = n*2-1
    for i in range(n):
        txt += f' {i+1}'
        print(f'{txt.strip():^{m}}')
main(int(input()))
