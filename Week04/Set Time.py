"""Set Time"""
def settime(t) :
    """Set Time"""
    hour = t // (60*60)
    minute = (t % (60*60)) // 60
    sec = (t % (60*60)) % 60
    print(f"{hour:>02}:{minute:>02}:{sec:>02}")
settime(int(input()))
