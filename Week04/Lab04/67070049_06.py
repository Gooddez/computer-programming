"""ข้อ6"""
def main():
    with open("username.txt","w") as user,open("firstname.txt","r") as first,open("lastname.txt","r") as last:
        for i,j in zip(first,last):
            contain = i.split() + j.split()
            user.write(contain[1][0].lower()+contain[3][:6].capitalize()+contain[2][-3:]+"\n")
main()