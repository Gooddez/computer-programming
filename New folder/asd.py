"""asdad"""
salary = int(input())
salary *= 12 #เงินรายปี
if salary * 0.5 >= 100000: # หารายได้สุทธิ หักค่าใช้ไม่เกิน 100,000
    salary-=100000
else: # หารายได้สุทธิ
    salary -= salary * 0.5
pay = 0 #จำนวนเงินที่ต้องจ่าย
tax = 0 # % ภาษี
l = [150000,150000,200000,250000,250000,1000000,3000000] #ช่วงที่คำนวณภาษีในแต่ระ
for i in l:
    if salary >= i:
        pay += i*tax
        salary -= i
    else:
        pay += salary * tax
        salary -= salary
    tax += 0.05
if salary:
    pay += salary * 0.35
print(int(pay))
