"""ข้อ3"""
def main(file,word):
    with open(file, "r") as data:
        data1 = data.read()
        print(data1.count(word))
main(input(),input())