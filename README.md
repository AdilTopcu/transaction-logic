# Bankamatik Uygulaması

## Proje Açıklaması

Bu proje, kullanıcıların hesap numarası ve çekmek istedikleri miktarı girerek bakiyelerini kontrol edebileceği ve para çekme işlemleri gerçekleştirebileceği bir bankamatik uygulamasıdır. Uygulama, kullanıcıların hesap bakiyeleri ve ek hesap bakiyeleri doğrultusunda işlem yapmalarına olanak tanır.

## Özellikler

- Kullanıcılar, kendi hesap numaralarını girerek bakiyelerini kontrol edebilir.
- Para çekme işlemi yapılırken, kullanıcının hesabında yeterli bakiye yoksa ek hesap bakiyesi kullanılabilir.
- Uygulama, erkek ve kadın kullanıcılar için farklı hitaplar kullanarak kişiselleştirilmiş bir deneyim sunar.

## Kullanıcı Hesapları

Aşağıda örnek kullanıcı hesapları yer almaktadır:

- **Adil**: 
  - Hesap No: 11111
  - Bakiye: 13000
  - Ek Hesap Bakiye: 12000
  
- **Mete**: 
  - Hesap No: 22222
  - Bakiye: 4000
  - Ek Hesap Bakiye: 2500

- **Mustafa**: 
  - Hesap No: 33333
  - Bakiye: 63000
  - Ek Hesap Bakiye: 22000

- **Melis**: 
  - Hesap No: 44444
  - Bakiye: 16000
  - Ek Hesap Bakiye: 10000

- **Nurcan**: 
  - Hesap No: 55555
  - Bakiye: 33000
  - Ek Hesap Bakiye: 22000

- **Serap**: 
  - Hesap No: 66666
  - Bakiye: 34000
  - Ek Hesap Bakiye: 32000

## Kullanım

### Adım 1: Hesap Numarası ve Miktar Girişi
Kullanıcı, hesap numarasını ve çekmek istediği miktarı girer. 

### Adım 2: Bakiye Kontrolü
Uygulama, kullanıcının bakiyesini ve ek hesap bakiyesini kontrol eder. Eğer kullanıcı yeterli bakiyeye sahipse işlem başarılı bir şekilde gerçekleşir.

- Eğer kullanıcı hesabında yeterli bakiye yoksa, ek hesap bakiyesini kullanma seçeneği sunulur.
- Eğer ek hesap bakiyesi de yetersizse, işlem yapılmaz ve kullanıcıya bir uyarı mesajı gösterilir.

### Adım 3: Hitap Kullanımı
Uygulama, kullanıcının cinsiyetine göre uygun hitap kullanır:
- Erkek kullanıcılar için: "Bey"
- Kadın kullanıcılar için: "Hanım"

## Kod Yapısı

Bu projede aşağıdaki işlevsellikler mevcuttur:

1. **Hesap Veritabanı**: Farklı kullanıcıların hesap bilgileri birer sözlük (dictionary) olarak tanımlanmıştır.
2. **Para Çekme Fonksiyonu**: `cekimYapma()` fonksiyonu, bir kullanıcının hesap bakiyesini kontrol eder ve para çekme işlemini gerçekleştirir.
3. **Hesap Numarası ile Kullanıcı Arama**: Kullanıcıdan alınan hesap numarasına göre, doğru kullanıcı bulunur ve işlemi gerçekleştiren fonksiyon çağrılır.
4. **Hitap Mesajı**: Kullanıcının cinsiyetine göre doğru hitap mesajı görüntülenir.

## Kullanıcıdan Giriş

Kullanıcıdan alınan bilgiler:
- **Hesap Numarası**: Kullanıcıdan hesap numarası alınır.
- **Çekmek İstenilen Miktar**: Kullanıcıdan çekmek istediği miktar alınır.

## Ekstra Özellikler

- **Yetersiz Bakiye Durumu**: Kullanıcıda yeterli bakiye yoksa, ek hesap kullanımı önerilir.
- **Hesap Numarası Hatası**: Sistemde bulunmayan bir hesap numarası girildiğinde kullanıcıya hata mesajı verilir.

## Kurulum

Proje, Python ile çalışacak şekilde yazılmıştır. Projeyi çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Python 3'ün yüklü olduğundan emin olun.
2. Proje dosyasını bilgisayarınıza indirin.
3. Dosyayı bir terminal veya komut satırında çalıştırın.
