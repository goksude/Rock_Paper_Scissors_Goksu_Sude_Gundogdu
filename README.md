# Taş, Kağıt, Makas Oyunu

## Oyun Kuralları

- **Taş** makası yener.
- **Makas** kağıdı yener.
- **Kağıt** taşı yener.
- Oyun birden fazla turdan oluşur.
- Her tur sonunda kazanan belirlenir ve oyunun genel galibi, iki tur kazanan taraf olur.

## Nasıl Oynanır?
- Program çalıştırıldığında oyunun kuralları ekranda görüntülenir.
- Oyuncu, taş, kağıt veya makas seçeneklerinden birini yazarak seçim yapar.
- Bilgisayar, rastgele bir seçim yapar.
- Kazanan tur sonunda belirlenir.
- İlk iki turu kazanan genel oyunun galibi olur.
- Oyun sonunda, tekrar oynayıp oynamak isteyip istemediğiniz sorulur. Cevabınıza göre oyun yeniden başlar veya sona erer.

## Teknik Detaylar
- Dil: Python 3
- Rastgele Seçim: Bilgisayarın seçimi, Python’un random modülü ile rastgele olarak belirlenir.
- Koşullu İfadeler: Oyuncu ve bilgisayarın seçimine göre sonuçlar, if-else yapılarıyla kontrol edilir.
- Döngüler: Oyun, birden fazla tur içerdiği için while döngüleri kullanılarak sürdürülür.
- Kullanıcı Girişi: Oyuncunun seçimi input() fonksiyonu ile alınır ve küçük harflere (lower()) dönüştürülerek doğrulanır.
