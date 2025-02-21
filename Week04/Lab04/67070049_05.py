"""ข้อ5"""
def main(file):
    with open(file,"r") as data:
        alldata = data.read().split()
        sumof = 0
        for i in alldata:
            sumof += float(i)
        print(f'{sumof / len(alldata):.5f}')
main(input())