"""Donut"""
def main(a,b,c,d):
    """Donut"""
    first = d//(b+c)*c
    paid1 = (d-first)//b*b
    free = paid1//b*c
    extrapaid = 0
    if d-(paid1+free)>0:
        extrapaid = d-(paid1+free)
    price = (paid1 + extrapaid)*a
    amount = free+paid1+extrapaid
    print(price,amount)
main(int(input()),int(input()),int(input()),int(input()))
