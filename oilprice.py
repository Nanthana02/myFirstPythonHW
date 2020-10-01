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
    print("#                                  Welcome                                     #")
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

def menu5():
    print("################################################################################")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                                                              #")
    print("#                                เลือกการทำงานของโปรแกรม...                     #")
    print("#                            1. ออกจากโปรแกรม                                  #")
    print("#                            2. เริ่มการทำงานใหม่อีกครั้ง                            #")
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
    a = 0
    while not(a in [1]):
        menu1()
        b = input("กด 1 เพื่อเริ่มการทำงาน : ")
        if b.isnumeric():
            a = int(b)

        else:
            a = 0

    x = 0
    while not(x in [1, 2, 3, 4, 5, 6]):
        menu2()
        y = input("กรุณาเลือกชนิดเชื้อเพลิง :")
        if y.isnumeric():
            x = int(y)

        else:
            x = 0

    a = 0
    while not(a in [1, 2]):
        menu3()
        z = input("เลือกชนิดการคำนวนข้อมูล :")
        if z.isnumeric():
            a = int(z)
        else:
            a = 0

    a = 0
    while not(a):
        menu4()
        g = input("กรุณาใส่ค่าการคำนวน :")
        if g.isnumeric():
            a = float(g)
        else:
            a = 0
        g = float(g)
        if z == '1':
            if y == '1':
                a = g / 29.16
                print("จำนวน = {}ลิตร".format(a))
            elif y == '2':
                a = g / 25.30
                print("จำนวน = {}ลิตร".format(a))
            elif y == '3':
                a = g / 21.68
                print("จำนวน = {}ลิตร".format(a))
            elif y == '4':
                a = g / 20.2
                print("จำนวน = {}ลิตร".format(a))
            elif y == '5':
                a = g / 21.0
                print("จำนวน = {}ลิตร".format(a))
            elif y == '6':
                a = g / 21.1
                print("จำนวน = {}ลิตร".format(a))
            else:
                print("can not calculate")

        if z == '2':
            if y == '1':
                a = g * 29.16
                print("จำนวเงิน = {}บาท".format(a))
            elif y == '2':
                a = g * 25.30
                print("จำนวเงิน = {}บาท".format(a))
            elif y == '3':
                a = g * 21.68
                print("จำนวเงิน = {}บาท".format(a))
            elif y == '4':
                a = g * 20.2
                print("จำนวเงิน = {}บาท".format(a))
            elif y == '5':
                e = g * 21.0
                print("จำนวเงิน = {}บาท".format(a))
            elif y == '6':
                e = f / 21.1
                print("จำนวเงิน = {}บาท".format(a))
            else:
                print("can not calculate")
    p = input("กดปุ่มใดๆเพื่อเลือกการทำงานของโปรแกรม")

    a = 0
    while not(a in [1, 2]):
        menu5()
        b = input("เลือกออกจากโปรแกรม :")
        if b.isnumeric():
            a = int(b)
        else:
            a = 0
    if a == 1:
        break
