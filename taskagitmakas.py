import random


def tas_kagit_makas_Goksu_Sude_Gundogdu():
    print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
    print("Oyun kuralları: Taş makası yener, makas kağıdı yener, kağıt taşı yener.")
    print("İlk iki turu kazanan oyunu kazanır.")

    while True:
        secenekler = ["taş", "kağıt", "makas"]
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0
        oyun_turu = 0

        while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            print(f"\nTur {oyun_turu + 1}")
            oyuncu_secimi = input("Lütfen seçiminizi yapın (taş, kağıt, makas): ").lower()

            if oyuncu_secimi not in secenekler:
                print("Geçersiz bir seçenek girdiniz, lütfen tekrar deneyin.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                    (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                    (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu siz kazandınız!")
                oyuncu_galibiyetleri += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_galibiyetleri += 1

            oyun_turu += 1

        if oyuncu_galibiyetleri == 2:
            print("\nTebrikler! Oyunu kazandınız!")
        else:
            print("\nBilgisayar oyunu kazandı. Başarılar dileriz!")

        devam_mi = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        bilgisayar_devam_mi = random.choice(["evet", "hayır"])
        print(f"Bilgisayarın devam etme isteği: {bilgisayar_devam_mi}")

        if devam_mi != "evet" or bilgisayar_devam_mi != "evet":
            print("Oyun sona erdi. Teşekkürler!")
            break


# Oyunu başlatmak için fonksiyonu çağırabilirsiniz
tas_kagit_makas_Goksu_Sude_Gundogdu()
