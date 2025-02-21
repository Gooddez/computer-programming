"""P'Chang"""
def main(menu,t,q,premium):
    """P'Chang"""
    menus = {
        "Suki Haeng Tha le Khai dao Phet Noi Sai Sauce Yer Yer":1049,
        "Kaphrao Mu Krop Pri Sret Mai Phrik Khai dao Khai daeng Keop Suk":346,
        "Mu Sap Phat NammanHoi Khai dao Vegan":3,
        "Kaengsom Saeb Saeb":124,
        "Sapa Ket Ti Kha Bo Na Ra":1832,
    }
    if menu not in menus:
        ans = "00 days 00 hours 00 mins 00 secs."
    else:
        if premium.lower() == "yes":
            time = menus[menu] * t
        else:
            time = (menus[menu] * t) + (q * 30 * 60)
        day = time//(24*60*60)
        time %= (24*60*60)
        hour = time//(60*60)
        time%=60*60
        minute = time//60
        time%=60
        if day >= 3 and (hour > 0 or time > 0 or minute > 0):
            ans = f"{int(day):>02} days {int(hour):>02} hours \
{int(minute):>02} mins {int(time):>02} secs.\nYou've starved to death."
        else:
            ans = f"{int(day):>02} days {int(hour):>02} hours \
{int(minute):>02} mins {int(time):>02} secs."
    return ans
print(main(input(),float(input()),float(input()),input()))
