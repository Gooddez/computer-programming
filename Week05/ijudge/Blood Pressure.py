"""Blood Pressure"""
def main(sbp,dbp):
    """Blood Pressure"""
    if sbp > 140 or dbp > 90:
        ans = "Hypertension"
    else:
        ans = "Normal"
    return ans
print(main(int(input()),int(input())))
