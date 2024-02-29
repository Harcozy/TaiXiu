import random
import time
import termcolor

doan_taixiu: str
base_money = 1000000
dat_cuoc: int
GiaTriDatCuoc = ["tai", "xiu", "tài", "xỉu"]

def clear():
    from os import system
    system("Pause")
    system("cls")
    
def TaiXiuAskingUser():
    global doan_taixiu
    global base_money
    global dat_cuoc
    global GiaTriDatCuoc
    
    print(f"Welcome to tai xiu digital!\nYour money now is: {base_money}\n\n")
    print("Đoán", termcolor.colored("Tài", "red") ,"hay", termcolor.colored("Xỉu", "green") ,": ", end= '')
    doan_taixiu = str(input()).lower()
    if doan_taixiu not in GiaTriDatCuoc:
        print("Vui lòng nhập lại")
        time.sleep(3)
        clear()
        TaiXiuAskingUser()
    print("Số",termcolor.colored("tiền", 'green'),"bạn muốn đặt cược: ", end= '')
    dat_cuoc = int(input())
    if dat_cuoc > base_money:
        print(termcolor.colored("Không đủ", 'red'),termcolor.colored("số tiền", 'green'),termcolor.colored("để đặt cược!", 'red'))
        clear()
        TaiXiuAskingUser()
    else:
        base_money -= dat_cuoc
    
        

#Tai Xiu
while True:  
    TaiXiuAskingUser()
    xuc_sac_1 = random.randint(1, 6)
    xuc_sac_2 = random.randint(1, 6)
    xuc_sac_3 = random.randint(1, 6)
    xiu = (xuc_sac_1 + xuc_sac_2 + xuc_sac_3 <= 10)
    tai = (xuc_sac_1 + xuc_sac_2 + xuc_sac_3 >= 11 <= 18)

    if tai:
        print(termcolor.colored("Tài", "red"))
        if doan_taixiu == "tai":
            base_money += dat_cuoc * 2
            print(termcolor.colored("Chúc mừng", "yellow"),", bạn đã ",termcolor.colored("thắng", "green")," :>>!\n\n\n")
            clear()
        else:
            print(termcolor.colored("Bạn không nhận được gì cả!", "red"),"\n\n\n")
            clear()
    if xiu:
        print(termcolor.colored("Xỉu", "green"))
        if doan_taixiu == "xiu":
            base_money += dat_cuoc * 2
            print(termcolor.colored("Chúc mừng", "yellow"),", bạn đã ",termcolor.colored("thắng", "green")," :>>!\n\n\n")
            clear()
        else:
            print(termcolor.colored("Bạn không nhận được gì cả!", "red"),"\n\n\n")
            clear()
