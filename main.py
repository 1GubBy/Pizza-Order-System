import csv
from datetime import datetime
from pathlib import Path
import time
import pizzas  #pizza ve sos sınıflarımın bulunduğu dosyaları burada kullanabilmek için import ettim
import sauces


def main():

    global title

    global pizza_tabani
    global sos

    global description
    global cost

    checkPoint = 1
   
    
    file_path = "menu.txt"   # menu.txt'nin yolunu kolaylık olması için değişkene atadım
    path = Path(file_path)
    
    if (path.is_file):  # menünün var olup olmadığını kontrol ettik 

            menu = open(file_path, mode="r", encoding="utf-8")  # türkçe karakterleri sorunsuz bastırmak için utf-8 formatında okuduk.
            print(menu.read())  # menüyü ekrana yazdırdık.

            print("---------------------------" + "\n")

            pizza_tabani = int(input("İlk Olarak Pizza Tabanınızı Seçiniz (Tabanın Başındaki Rakamı Giriniz) : "))
            calculateCost(pizza_tabani)

            sos = int(input("İstediğiniz Bir Adet Sosu Seçiniz (Sos'un Başındaki Sayıyı Giriniz) : ")) 
            calculateCost(0, sos)

            """  tekrarlı seçim yaptırma denemesi
            while checkPoint == 1:
                checkPoint = int(input("Tekrardan Taban Seçimi Yapmak İstiyorsaniz 1'e , Sos Seçimine Geçmek İstiyorsaniz 2'ye Basınız : "))

                match checkPoint:
                    case 1:
                        pizza_tabani = int(input("Lütfen Pizza Tabanınızı Seçiniz (Tabanın Başındaki Rakamı Giriniz) : "))
                        calculateCost(pizza_tabani)
                        checkPoint = int(input("Tekrardan Taban Seçimi Yapmak İstiyorsaniz 1'e , Sos Seçimine Geçmek İstiyorsaniz 2'ye Basınız : "))
                    
                        if checkPoint == 1:
                            checkPoint = repeatSelection()
                            
                            match checkPoint:
                                case 1:
                                    checkPoint = repeatSelection()
                                case 2:
                                    sos = int(input("İstediğiniz Bir Adet Sosu Seçiniz (Sos'un Başındaki Sayıyı Giriniz) : "))
                                    calculateCost(0, sos)

                        elif checkPoint == 2:
                            sos = int(input("İstediğiniz Bir Adet Sosu Seçiniz (Sos'un Başındaki Sayıyı Giriniz) : ")) 
                            calculateCost(0, sos)
                    case 2:
                        sos = int(input("İstediğiniz Bir Adet Sosu Seçiniz (Sos'un Başındaki Sayıyı Giriniz) : "))
                        calculateCost(0, sos)"""
                        
    else:
        print("menu.txt dosyası mevcut değil.")    

# gelen taban veya sos değerlerine göre toplam tutarın hesaplandığı, pizza açıklamalarının düzenlendiği fonskiyon
def calculateCost(taban = 0, sos = 0):
    global cost
    global description
    global title

    classic_pizza = pizzas.ClassicPizza()
    margherita_pizza = pizzas.MargheritaPizza()
    turk_pizza = pizzas.TurkPizza()
    sade_pizza = pizzas.SadePizza()

    zeytin = sauces.Zeytin()
    mantar = sauces.Mantar()
    keciPeyniri = sauces.KeciPeyniri()
    et = sauces.Et()
    sogan = sauces.Sogan()
    misir = sauces.Misir()

    
    match taban:
        case 1:
            cost = classic_pizza.get_cost(classic_pizza.cost)
            description = classic_pizza.get_description(classic_pizza.description)
            title = "Klasik Pizza"
        case 2:
            cost = margherita_pizza.get_cost(margherita_pizza.cost)
            description = margherita_pizza.get_description(margherita_pizza.description)
            title = "Margherita Pizza"
        case 3:
            cost = turk_pizza.get_cost(turk_pizza.cost)
            description = turk_pizza.get_description(turk_pizza.description)
            title = "Türk Pizza"
        case 4:
            cost = sade_pizza.get_cost(sade_pizza.cost)
            description = sade_pizza.get_description(sade_pizza.description)
            title = "Sade Pizza"
        case _:
            pass    

    match sos:
        case 11:
            cost = cost + zeytin.get_cost(zeytin.cost)
            title = title + " ve " + "Zeytin"
            print(f"Toplam Tutar : {cost} TL \nSipariş Özetiniz : {title}\nÖdeme Sayfasına Yönlendiriliyorsunuz...\n")
            time.sleep(1)
            getUserInformations()      
        case 12:
            cost = cost + mantar.get_cost(mantar.cost)
            title = title + " ve " + "Mantar"
            print(f"Toplam Tutar : {cost} TL \nSipariş Özetiniz : {title}\nÖdeme Sayfasına Yönlendiriliyorsunuz...\n")
            time.sleep(1)
            getUserInformations() 
        case 13:
            cost = cost + keciPeyniri.get_cost(keciPeyniri.cost)
            title = title + " ve " + "Keçi Peyniri"
            print(f"Toplam Tutar : {cost} TL \nSipariş Özetiniz : {title}\nÖdeme Sayfasına Yönlendiriliyorsunuz...\n")
            time.sleep(1)
            getUserInformations()          
        case 14:
            cost = cost + et.get_cost(et.cost)
            title = title + " ve " + "Et"
            print(f"Toplam Tutar : {cost} TL \nSipariş Özetiniz : {title}\nÖdeme Sayfasına Yönlendiriliyorsunuz...\n")
            time.sleep(1)
            getUserInformations()  
        case 15:
            cost = cost + sogan.get_cost(sogan.cost)
            title = title + " ve " + "Soğan" 
            print(f"Toplam Tutar : {cost} TL \nSipariş Özetiniz : {title}\nÖdeme Sayfasına Yönlendiriliyorsunuz...\n")
            time.sleep(1)  
            getUserInformations()        
        case 16:
            cost = cost + misir.get_cost(misir.cost)
            title = title + " ve " + "Mısır" 
            print(f"Toplam Tutar : {cost} TL \nSipariş Özetiniz : {title}\nÖdeme Sayfasına Yönlendiriliyorsunuz...\n")
            time.sleep(1)
            getUserInformations() 
        case _:
            pass       

# pizza tabanının tekrardan seçilme işlemini sağlar
def repeatSelection():
        pizza_tabani = int(input("Lütfen Pizza Tabanınızı Seçiniz (Tabanın Başındaki Rakamı Giriniz) : "))
        calculateCost(pizza_tabani)  # girilen yeni tabana göre tekrardan yeni ücreti hesaplar.
        checkPoint = int(input("Teekrardan Taban Seçimi Yapmak İstiyorsaniz 1'e , Sos Seçimine Geçmek İstiyorsaniz 2'ye Basınız : "))
        
        return checkPoint

# kullanıcının isim ve kart bilgilerini almamızı sağlayan fonksiyon
def getUserInformations():
    
    # flag ve while yapısı sayesinde istediğim şartları sağlayacak şekilde veri girişi yapılana kadar tekrar giriş yapılmasını sağladım.

    flag = 0

    while flag == 0:
        userName = input("Adınızı ve Soyadınızı Giriniz: ")

        if userName != '' and all(chr.isalpha() or chr.isspace() for chr in userName):  # girilecek isim sadece boşluk ve alfabetik karakterler içerebilir (sayı, özel karakterler girilememsi için sınırlama yaptım)
            flag = 1
        else :
            print("GEÇERSİZ GİRİŞ\nGirmiş olduğunuz isim geçersiz karakterler içermektedir.Lütfen uygun bir şekilde tekrardan giriniz.\n")
            
    flag = 0

    while flag == 0:
        userID = input("TC Kimlik Numaranızı Giriniz: ")

        if userID.upper().isupper() :
            print("GEÇERSİZ GİRİŞ\nGirmiş olduğunuz kimlik numarası karakter içermektedir.Lütfen uygun bir şekilde tekrardan giriniz.\n")
        elif len(userID) != 11:
            print("GEÇERSİZ GİRİŞ\nGirmiş olduğunuz kimlik numarası 11 hane olmalıdır.Lütfen uygun bir şekilde tekrardan giriniz.\n")     
        else:
            flag = 1

    flag = 0

    while flag == 0:
        userCreditCardNumber = input("Kredi Kart Numaranızı Giriniz: ")

        if userCreditCardNumber.upper().isupper() :
            print("GEÇERSİZ GİRİŞ\nGirmiş olduğunuz kimlik numarası karakter içermektedir.Lütfen uygun bir şekilde tekrardan giriniz.\n")
        elif len(userCreditCardNumber) != 16:
            print("GEÇERSİZ GİRİŞ\nGirmiş olduğunuz kart numarası 16 hane olmalıdır.Lütfen uygun bir şekilde tekrardan giriniz.\n")     
        else:
            flag = 1

    flag = 0

    while flag == 0:
        
        userCreditCardPassword = input("Kredi Kartınızın Şifresini Giriniz: ")

        if userCreditCardPassword.upper().isupper() :
            print("GEÇERSİZ GİRİŞ\nGirmiş olduğunuz şifre karakter içermektedir.Lütfen uygun bir şekilde tekrardan giriniz.\n")
        elif len(userCreditCardPassword) != 4:
            print("GEÇERSİZ GİRİŞ\nGirmiş olduğunuz kart şifresi 4 hane olmalıdır.Lütfen uygun bir şekilde tekrardan giriniz.\n")     
        else:
            flag = 1
    
    saveDatas(userName, userID, userCreditCardNumber, userCreditCardPassword)  # alınan bilgileri dosyaya kaydetmek için gerekli fonksiyonu kullandım
    
# Kullanıcıya ait bilgileri ve diğer sipariş detaylarını csv dosyası içerisine yazdırdığımız fonskiyon
def saveDatas(userName, userID, userCreditCardNumber, userCreditCardPassword):
    
    userCreditCardNumber = splitData(userCreditCardNumber, 4) # kart numarasına 4 karakterde bir boşluk ekledik
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # anlık saat ve tarih bilgisini aldık, strftime() ile istediğim şekilde tekrardan düzenledim

    
    with open("orderDetails.csv", mode="a", encoding="utf-8" ) as csvfile:
            
            fieldnames = ["Müşteri Adı Soyadı ", " TC Kimlik Numarası ", " Kredi Kart Numarası ", " Kredi Kart Şifresi "]
            writer = csv.DictWriter(csvfile, delimiter=',',fieldnames = fieldnames)
            writer.writeheader()
            writer.writerow({"Müşteri Adı Soyadı " : " " + userName, " TC Kimlik Numarası " : " " +  userID, " Kredi Kart Numarası " : " " +  userCreditCardNumber, " Kredi Kart Şifresi " : " " +  userCreditCardPassword})
            
            fieldnames2 = ["Verilen Pizza ", " Tutarı ", " Sipariş Tarihi ", " Sipariş Açıklaması "]
            writer = csv.DictWriter(csvfile, delimiter=',',fieldnames = fieldnames2)
            writer.writeheader()
            writer.writerow({"Verilen Pizza " : " " + title  , " Tutarı " : " " +  f"{cost} TL",  " Sipariş Tarihi " : " " + date, " Sipariş Açıklaması " : " " +  description})

            csvfile.close()
            
# Gelen kredi kartı numarasını 4'lü öbekler halinde tekrardan düzenler (4 -> size değeridir, Yukarıda fonskiyonu çağırırken 4 girilmiştir.)
def splitData(creditCardNumber, size): 
    return ' '.join(creditCardNumber[i:i+size] for i in range(0,len(creditCardNumber), size))

main()






