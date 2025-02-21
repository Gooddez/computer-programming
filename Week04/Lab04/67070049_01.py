"""ข้อ1"""
def main(text):
    with open("name.txt", "a") as file:
        file.write("\n"+text)
main(input())