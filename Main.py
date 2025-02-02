def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Hata! Sıfıra bölme yapılamaz."
    return a / b

def hesap_makinesi():
    while True:
        print("\nKebabistik Hesap Makinesi")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Çıkış")
        
        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1/2/3/4/5): ")
        
        if secim == '5':
            print("Hesap makinesi kapatılıyor...")
            break
        
        if secim not in ('1', '2', '3', '4'):
            print("Geçersiz seçim, lütfen tekrar deneyin.")
            continue
        
        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Hata! Lütfen geçerli bir sayı girin.")
            continue
        
        if secim == '1':
            print("Sonuç:", toplama(sayi1, sayi2))
        elif secim == '2':
            print("Sonuç:", cikarma(sayi1, sayi2))
        elif secim == '3':
            print("Sonuç:", carpma(sayi1, sayi2))
        elif secim == '4':
            print("Sonuç:", bolme(sayi1, sayi2))

if __name__ == "__main__":
    hesap_makinesi()
