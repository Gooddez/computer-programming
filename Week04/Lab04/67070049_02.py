"""ข้อ2"""
def main(text):
    with open("question2.txt", "w") as file:
        file.write("\n".join(text))
main(input().split(","))