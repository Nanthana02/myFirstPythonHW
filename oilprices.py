def menu1():
    print("################################################################################")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                  Wellcom                                     #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("################################################################################")


def menu2():
    print("################################################################################")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                  รายการ                                      #")
    print("#                                                                              #")
    print("#                     1.Gasoline 95  ราคา 29.16 BAHT                           #")
    print("#                     2.Gasoline 91  ราคา 25.30 BAHT                           #")
    print("#                     3.Gasohol 91   ราคา 21.68 BAHT                           #")
    print("#                     4.Gasohol E20  ราคา 20.2  BAHT                           #")
    print("#                     5.Gasohol 95   ราคา 21.2  BAHT                           #")
    print("#                     6.Diesel       ราคา 21.1  BAHT                           #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("################################################################################")


def menu3():
    print("################################################################################")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                ชนิดการทำงาน                                   #")
    print("#                                                                              #")
    print("#                           1.คำนวนจากเงินเป็นลิตร                                #")
    print("#                           2.คำนวนจากลิตรเป็นเงิน                                #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("################################################################################")


def menu4():
    print("################################################################################")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                             กรุณาใส่จำนวนเงิน                                   #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("################################################################################")


while True:

    menu1()
    b = input("กดEnterเพื่อดำเนินการต่อ")

    a = 0
    while not(a in [1, 2, 3, 4, 5, 6]):
        menu2()
        b = input("เลือกเชื้อเพลิง :")
        if b.isnumeric():
            a = int(b)
    else:
        a = 0

    a = 0
    while not(a in [1, 2]):
        menu3()
        b = input("เลือกชนิดการทำงาน :")
        if b.isnumeric():
            a = int(b)
    else:
        a = 0

if a == 1:
	money = float(input("จำนวนเงิน (บาท) : "))
	print('จำนวนเงิน ',money,' บาท เท่ากับ ',round(money/i,2),' ลิตร')

elif a == 2:
	money = float(input("จำนวนลิตร (ลิตร) : "))
	print('จำนวนลิตร ',money,' ลิตร เท่ากับ ',round(money*i,2),' บาท')
    

	if '1' in a:
		a = float(input("จำนวนเงิน : "))
	menu4()
	if b.isnumeric():
		if a == 1:
			t = b/29.16
			print('t', '%.2f' % b, 'BATH')
		elif a == 2:
			t = b/25.30
			print('t', '%.2f' % b, 'BATH')
		elif a == 3:
			t = b/21.68
			print('t', '%.2f' % b, 'BATH')
		elif a == 4:
			t = b/20.2
			print('t', '%.2f' % b, 'BATH')
		elif a == 5:
			t = b/21.2
			print('t', '%.2f' % b, 'BATH')
		elif a == 6:
			t = b/21.1
			print('t', '%.2f' % b, 'BATH')

