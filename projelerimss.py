##BANKAMATIK UYGULAMASI
adilHesap = {
    'ad' : 'Adil',
    'cinsiyet' : 'erkek',
    'hesapNo' : '11111',
    'bakiye' : 13000,
    'ekHesapBakiye' : 12000
}
meteHesap = {
    'ad' : 'Mete',
    'cinsiyet' : 'erkek',
    'hesapNo' : '22222',
    'bakiye' : 4000,
    'ekHesapBakiye' : 2500
}
mustafaHesap = {
    'ad' : 'Mustafa',
    'cinsiyet' : 'erkek',
    'hesapNo' : '33333',
    'bakiye' : 63000,
    'ekHesapBakiye' : 22000
}
melisHesap = {
    'ad' : 'Melis',
    'cinsiyet' : 'kız',
    'hesapNo' : '44444',
    'bakiye' : 16000,
    'ekHesapBakiye' : 10000
}
nurcanHesap = {
    'ad' : 'Nurcan',
    'cinsiyet' : 'kız',
    'hesapNo' :'55555',
    'bakiye' : 33000,
    'ekHesapBakiye' : 22000
}
serapHesap = {
    'ad' : 'Serap',
    'cinsiyet' : 'kız',
    'hesapNo' : '66666',
    'bakiye' : 34000,
    'ekHesapBakiye' : 32000
}

# Kullanıcıdan hesap numarası ve çekmek istediği miktar
kullanici_hesap_no = input("Hesap numaranızı giriniz: ")
miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))

# Kullanıcıların hesap bilgilerini içeren liste
kullanici_listesi = [adilHesap, meteHesap, mustafaHesap, melisHesap, nurcanHesap, serapHesap]

def cekimYapma(kullanici, miktar):
    global adilHesap, meteHesap, mustafaHesap, melisHesap, nurcanHesap, serapHesap
    print(f"Merhaba {kullanici['ad']} {hitap}")
    toplamPara = kullanici['bakiye'] + kullanici['ekHesapBakiye']
   
    if toplamPara >= miktar:
        if kullanici['bakiye'] >= miktar:
        
            kullanici['bakiye'] -= miktar
            print(f"Para çekim işleminiz başarıyla sonuçlandı. Güncel bakiyeniz: {kullanici['bakiye']}")
        else:
            ekHesapKullanimi = input('Hesap bakiyeniz yetersiz, ek hesap bakiyesini kullanmak ister misiniz? (E/H): ')
            if ekHesapKullanimi == 'E':
                kullanici['bakiye'] = 0
                kullanici['ekHesapBakiye'] -= (miktar - kullanici['bakiye'])
                print(f"Para çekim işleminiz başarıyla sonuçlandı. Güncel ek hesap bakiyeniz: {kullanici['ekHesapBakiye']}")
            elif ekHesapKullanimi == 'H':
                print("Üzgünüz, yetersiz bakiye.")
    else:
        print("Yetersiz bakiye. Lütfen ek hesap bakiyenizi yükseltmek için en yakın şubeye başvurunuz.")

# Hesap numarasına göre doğru kullanıcıyı bulma
for kullanici in kullanici_listesi:
    if kullanici['hesapNo'] == kullanici_hesap_no:
         if kullanici['cinsiyet'] == 'erkek':
          hitap='Bey'
          cekimYapma(kullanici, miktar)
          break
         else:
             hitap='Hanım'
         cekimYapma(kullanici, miktar)
         break
else:
 print("Hesap numaranız sistemde bulunamadı.")

