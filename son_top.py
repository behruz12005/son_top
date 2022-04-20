import random as r

def men_top():
    m = 1
    ran = r.randint(1,11)
    print("Men 1 dan 10 gacha son uyladim toping")
    while True:
        while True:
            men = input("son kriting: ")
            if men.isdigit():
                men = int(men)
                break
            else:
                print("Son kiriting!!")
        if men > ran:
            print("Yoq siz uylagan san menikadan katta kichik son uylang !!")
        elif men < ran:
            print("Yoq siz uylagan san menikadan kichik katta son uylang !!")
        else:
            print("Siz topdingiz")
            break
        m +=1
    print(f"Siz {m} urinshda topdingiz")
    return m
def sen_top():
    k = 1
    input("Sen bironta 10 gacha bulgan son uyla men topaman boshlash = enter")
    max = 11
    min= 1
    list = []
    while True:
        ran1 = r.randint(min,max)
        while ran1 in list:
            ran1 = r.randint(min,max)
        list.append(ran1)
        sen = input(f"Sen {ran1} raqqam uylaganmiding topgan bulsa = t  yoki katta bulsa = - yoki kichik bulsa = + >>: ")
        if sen == "t":
            break
        elif sen == '-':
            max-=1
        elif sen == '+':
            min+=1
        k +=1
        print(list)
    print(f"men Sizni {k} urinishda topdim")
    return k
def hisob():
    input("Son top uyiniga xush kelibsiz boshlash enter: ")
    while True:
        men = men_top()
        sen = sen_top()
        if men < sen:
            print(f"Siz yutingiz {men} urinish bilan tabriklaymiz u {sen} urinish bilan yutqazdi ")
        elif men > sen:
            print(f"Sen yutqazding hahaha {men} urinish bilan man {sen} topdim ukam")
        else:
            print("Dustlik g'alaba qozondi tbriklaymiz hammani raxmat raxmat")
        yana = input("Yana uymizmi hisobmi kurib turibsanku exit = no: ")
        if yana == "no":
            break
hisob()



