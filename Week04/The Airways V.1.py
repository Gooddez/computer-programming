"""The Airways V.1"""
def airway(b,out,a) :
    """The Airways V.1"""
    arrive = []
    for i in out:
        i = str(int(i)+2)
        arrive.append(f"{i:>02}")
    print(f"{b}: {"-".join(out)}")
    print(f"{a}: {"-".join(arrive)}")
airway(input(),input().split("-"),input())
