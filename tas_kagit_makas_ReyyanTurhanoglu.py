

bilgisayar=0
oyuncu=0
tur=1
oyun=1
bilgisayargenelskor=0
oyuncugenelskor=0

def tas_kagit_makas_REYYAN_TURHANOGLU():
    global bilgisayar
    global oyuncu
    global tur
    global oyun
    global bilgisayargenelskor
    global oyuncugenelskor
    
    bilgisayar = 0
    oyuncu = 0
    tur = 1
    import random
    kutlamaifadeleri=random.choice(["tebrikler","harikasınız","müthiş","böyle devam!","işte bu :)"])
    teselliifadeleri=random.choice(["bu tur olmadı","maalesef","üzgünüz","pes etmek yok","zamanla olacak"])
    yanıt = input("oynamaya hazırsan 'evet' yazman yeterli :) :")
    if yanıt!="evet":
        print('sanırım oyunu oynamaya hazır değilsin hazır olunca "evet" yazıp başla')
        tas_kagit_makas_REYYAN_TURHANOGLU()
    if yanıt == 'evet':
        print("oyun başlıyor")
        print('{:*^40}'.format("BAŞARILAR DİLERİZ"))
        print("çıkmak için 1 e basmanız yeterli")
        while True:
            if oyuncu == 2:
                print("tebrikler kazandınız")
                oyuncugenelskor += 1
                break
            if bilgisayar == 2:
                print("üzgünüz bilgisayar kazandı")
                bilgisayargenelskor += 1
                break
            print("{}. oyun {}. tur".format(oyun, tur))    
            print("taş ?-kağıt ?-makas ?")    
            seçenek = input("oyuncu:")
            if seçenek == "1":
                print("oyun sona erdi")
                break
            if seçenek not in ["taş", "kağıt", "makas"]:
                print("lütfen geçerli bir seçenek girin")
                continue
            import random
            cevap = random.choice(["taş", "kağıt", "makas"])
            if (seçenek == cevap):
                print("bilgisayar:", cevap)
                print("berabere!")
            elif (seçenek == "taş" and cevap == "makas") or (seçenek == "kağıt" and cevap == "taş") or (seçenek == "makas" and cevap == "kağıt"):
                print("bilgisayar:", cevap)
                print(kutlamaifadeleri,"bu turu oyuncu kazandı")
                oyuncu += 1
            else:
                print("bilgisayar:", cevap)
                print(teselliifadeleri,"bu turu bilgisayar kazandı")
                bilgisayar += 1
            print("Skor => oyuncu:", oyuncu, "- bilgisayar:", bilgisayar)
            tur += 1     

tas_kagit_makas_REYYAN_TURHANOGLU()

while oyuncu == 2 or bilgisayar == 2:
    print("{:~^50}".format("OYUNUN GENEL SKORU"))
    print("oyuncu:", oyuncugenelskor, "  ", "bilgisayar:", bilgisayargenelskor)
    tekrar1 = input("iyi yarıştınız tekrar oynamak ister misiniz?evet/hayır:")
    if(tekrar1!="evet" and tekrar1!="hayır"):
        print('lütfen "evet" ya da "hayır" cevabından birini girin.' )
        continue
    import random
    tekrar2 = random.choice(["evet", "hayır"])
    print("bilgisayarın cevabı:", tekrar2)
    if tekrar1 == "evet" and tekrar2 == "evet":
        print("ikiniz de tekrar oynamak istiyor")
        oyun+=1
        tas_kagit_makas_REYYAN_TURHANOGLU()
    else:
        print("oyuna devam edilmeyecek")
        break