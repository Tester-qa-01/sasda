print("Bankomatga xush kelibsiz")

print("Bankomat 2 ta kartani qollab quvvatlaydi 1) Humo 2) Uzcard")

turi = input("Qanday karta kiritasiz>> ").lower().strip()

if turi == "humo" or turi == "uzcard":
    karta = input("Karta raqamini kiriting: ")
    
    if len(karta) != 12:
        print("karta raqami 12 ta bolishi kerak")
    else:
        pin = input("karta parolini kiriting: ")

        if len(pin) != 4:
            print("xato parol kiritdingiz")
        else:
            print("parol togri kiritdingiz")
            if turi == "uzcard":
                hisob = 500_000
            else:
                hisob = 300_000
                
            for i in range(5):
                print("Xizmatlar:")
                print("1) Pin kodni o'zgartirish")
                print("2) Hisobni ko'rish")
                print("3) Xisobdan pul yechish")
                print("4) Chiqish")


                xizmatlar = int(input("Xizmat raqamini kiriting: "))

                if xizmatlar == 1:
                    eski_parol = input("Eski parolni kiriting: ")
                    
                    if eski_parol != pin:
                        print("parol xato")
                    else:
                        yangi_parol = input("yangi parol kiriting: ")
                        if len(yangi_parol) == 4:
                            print("parol ozgardi")
                            pin = yangi_parol

                elif xizmatlar == 2:
                    print(f"Xisobingizda {hisob} so'm mavjud")

                elif  xizmatlar == 3:
                    print("Yechishingiz mumkin bo'lgan summalar:")
                    print("1) 50000")
                    print("2) 200000")
                    print("3) 400000")
                    print("4) Boshqa summa")

                    tanla = input("Summalardan birini tanlang: ")

                    if tanla == "1":
                        ayir = 50000
                    elif tanla == "2":
                        ayir = 200000
                    elif tanla == "3":
                        ayir = 400000
                    elif tanla == "4":
                        kirit = input("Xoxlagan summani kiriting: ")
                        ayir = int(kirit)
                    else:
                        print("noto'g'ri tanlov qildingiz!")
                        ayir = 0
                        break

                    if ayir > hisob:
                        print("Hisobingizda mablag' yetarli emas!")

                    else:
                        hisob = hisob - ayir

                        print(f"Hisobingizda {hisob} so'm qoldi")
                elif xizmatlar == 4:
                    print("Foydalanganinigiz uchun rahmat")
                    break

else:
    print("notog'ri karta turini kiritdingiz")