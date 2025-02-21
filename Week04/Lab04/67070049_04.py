"""ข้อ4"""
def main(file):
    with open(file,"r") as data:
        alldata = data.read()
        print(alldata.count('\n')+1)
main(input())