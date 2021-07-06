import ssl
import sys
import waybackpy
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
from waybackpy.exceptions import WaybackError
from waybackpy import Url
from arayuz_kod import arayuz_1
from arayuz_kod import arayuz_2
from arayuz_kod import arayuz_3

url = input('Taramak istediginiz URL yi giriniz :  ') # URL girdisi al.
user_agent= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0"

arayuz_1()
secenek = input("Seciminiz: ")
print("-----------------------------------------------------------------")

try:
    if secenek == '1': # Mevcut sayfayi tarama
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        for c in comments:
            print(c)
            print("===========")
            c.extract()

    if secenek == '2': # wayback kullanilacaksa
        waybackpy_url = waybackpy.Url(url, user_agent)
        durum = waybackpy_url.JSON
        opt = durum['archived_snapshots']
        #print(durum['archived_snapshots'])
        list = {} # wayback machinede veri olup olmadigini kontrol etmek icin bos liste olusturup karsilastirdim.
        # print(durum)
        # archive.org da var olup olmadıgının kontrolu
        if opt != list: # eger varsa
            arayuz_2()
            wbSecenek = input("Seciminiz: ")
            print("-----------------------------------------------------------------")

            if wbSecenek == '1':
                oldest_archive_url = waybackpy.Url(url, user_agent).oldest()
                print("Ulasilan en eski URL: ",oldest_archive_url)

                page = requests.get(oldest_archive_url, verify=ssl.CERT_NONE)
                soup = BeautifulSoup(page.content, 'html.parser')
                comments = soup.find_all(string=lambda text: isinstance(text, Comment)) # commentlerin metnini cek
                for c in comments:
                    print(c)
                    print("---------------------------")
                    c.extract()

            if wbSecenek == '2':
                newest_archive_url = waybackpy.Url(url, user_agent).newest()
                print("Ulasilan en yeni URL: ",newest_archive_url)

                page = requests.get(newest_archive_url, verify=ssl.CERT_NONE)
                soup = BeautifulSoup(page.content, 'html.parser')
                comments = soup.find_all(string=lambda text: isinstance(text, Comment)) # commentlerin metnini cek
                for c in comments:
                    print(c)
                    print("---------------------------")
                    c.extract()

            if wbSecenek == '3':
                year = input("Aranan Wayback Yili: ") # eger aranan yila ait arsiv yoksa bulabildigi en eski sayfayi getirir.
                target_near = waybackpy_url.near(year)
                #print(target_near)

                print("Wayback URL:  ", target_near) # waybackteki istenene en yakin halinin urlsini gor --- kontrol

                page = requests.get(target_near) # wayback urlsine istek gonder. verify=ssl.CERT_NONE SSLError için cozum.

                soup = BeautifulSoup(page.content, 'html.parser') # beautiful soup ile ayikla.

                comments = soup.find_all(string=lambda text: isinstance(text, Comment)) # commentlerin metnini cek
                for c in comments:
                    print(c)
                    print("---------------------------")
                    c.extract()

            if wbSecenek == '4':
                print("Tarihleri girerken rakamlarin basina '0' koymayin! Ornek: 5")
                year = input("Aranan Wayback Yili: ") # eger aranan tarihe ait arsiv yoksa bulabildigi en eski sayfayi getirir.
                month = input("Ay: ")                 # ayni gun icinde birden fazla arsiv varsa en erken olani getirir.
                day = input("Gun: ")
                target_near = waybackpy_url.near(year, month, day)
                #print(target_near)

                print("Wayback URL:  ", target_near)

                page = requests.get(target_near, verify=ssl.CERT_NONE)
                soup = BeautifulSoup(page.content, 'html.parser') 

                comments = soup.find_all(string=lambda text: isinstance(text, Comment))
                for c in comments:
                    print(c)
                    print("---------------------------")
                    c.extract()

            # else:
            #     print("Hatali secim yaptiniz...")

        else:
            arayuz_3()
            kayit_secenek = input("Seciminiz: ")

            if kayit_secenek == '1':
                try:
                    archive = waybackpy_url.save() # eger waybackte yoksa su anki halini wb dbsine kaydet.
                except WaybackError as e:
                    pass

                newest_archive_url = waybackpy.Url(url, user_agent).newest()
                print("Kaydettiginiz URL: ",newest_archive_url)
                sys.exit()

            if kayit_secenek == '2':
                print("Çıkıldı!")
                sys.exit(0)

            else:
                sys.exit()

except KeyboardInterrupt:
    print ("\nCtrl+C'ye bastiniz...")
    sys.exit()

except:
    print("\nBir seyler ters gitti...")
    sys.exit()