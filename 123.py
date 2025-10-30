print("MINI MARKET KASSA DASTURI")

mahsulotlar = ["Non", "sut", "Yog'", "Shakar", "Un", "Tuxum"]
narxlar = [5000, 12000, 38000, 15000, 8000, 11000]

print("Mahsulotlar ro'yxati:")
for i in range(len(mahsulotlar)):
    print(f"{i+1}) {mahsulotlar[i]} - {narxlar[i]} so'm")

savat_nomi = []
savat_soni = []
savat_narxi = []

for i in range(3):
    tanlov = input(f"\n{i+1}-mahsulot raqamini tanlang (1-{len(mahsulotlar)}), yoki bo'sh tashlab keting: ").strip()

    if tanlov == "":
        print("Mahsulot tanlanmadi")
        savat_nomi.append("Olinmadi")
        savat_soni.append(0)
        savat_narxi.append(0)
    else:
        tanlov_index = int(tanlov) - 1
        mahsulot_nomi = mahsulotlar[tanlov_index]
        mahsulot_narxi = narxlar[tanlov_index]

        dona_str = input(f"{mahsulot_nomi} dan nechta olasiz? ").strip()
        dona = int(dona_str)

        umumiy_bir = dona * mahsulot_narxi

        savat_nomi.append(mahsulot_nomi)
        savat_soni.append(dona)
        savat_narxi.append(umumiy_bir)

        print(f"{dona} dona {mahsulot_nomi} ning narxi {umumiy_bir} so'm")

jami = 0
for summa in savat_narxi:
    jami = jami + summa

print("\n Xarid tugadi")
print(f"Umumiy: {jami} so'm")

if jami >= 100000:
    skidka = jami * 0.10
else:
    skidka = 0

yakuniy_summa = jami - skidka

print(f"Chegirma: {skidka} so'm")
print(f"To'lashingiz kere: {yakuniy_summa} so'm")

tolov_turi = input("\nTo'lov turi (naqt/plastik): ").strip().lower()

if tolov_turi == "naqt":
    print("\nNaqt pul qabul qilindi.")
    karta_turi = "Naqt"
    karta_balans = ""
    qolgan_balans = ""
elif tolov_turi == "plastik":
    karta_turi = input("Karta turi (humo/uzcard): ").strip().lower()

    if karta_turi == "uzcard":
        karta_balans = 300000
    elif karta_turi == "humo":
        karta_balans = 200000

    print(f"Kartadagi mavjud balans: {karta_balans} so'm")

    karta_raqam = input("Karta raqamini kiriting: ").strip()

    if len(karta_raqam) != 12:
        print("karta xato")
        exit()
    else:
        print("karta raqam togri")

    pin_kod = input("PIN kodni kiriting: ").strip()

    if karta_balans >= yakuniy_summa:
        qolgan_balans = karta_balans - yakuniy_summa
        print("To'lov plastik orqali qabul qilindi.")
    else:
        qolgan_balans = karta_balans
        print("Kartada yetarli mablag' yo'q.")

print("\n      CHEK")

print("Siz sotib oldingiz:")
for i in range(3):
    print(f"{i+1}) {savat_nomi[i]} | {savat_soni[i]} dona | {savat_narxi[i]} so'm")

print(f"\nJami: {jami} so'm")
print(f"Chegirma: {skidka} so'm")
print(f"To'lanadigan summa: {yakuniy_summa} so'm")

if tolov_turi == "naqt":
    print("To'lov turi: Naqt")
else:
    print(f"To'lov turi: Plastik ({karta_turi.upper()})")
    print(f"Kartadagi qolgan balans: {qolgan_balans} so'm")

