import ssl
import sys
import waybackpy
import requests
import urllib
from bs4 import BeautifulSoup
from bs4 import Comment
from waybackpy.exceptions import WaybackError
from waybackpy import Url
from arayuz_kod import arayuz_1
from arayuz_kod import arayuz_2
from arayuz_kod import arayuz_3
from arayuz_kod import arayuz_4
from termcolor import colored

print(colored("-----------------------------------------------------------------", 'yellow'))
url = input(colored('Taramak istediginiz URL yi giriniz: ', 'yellow'))
print(colored("-----------------------------------------------------------------", 'yellow'))
user_agent= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0"
robot_url = (url + "/robots.txt")

class Path():
    arayuz_1()
    print("-----------------------------------------------------------------")
    print("URL: ", robot_url)
    print("-----------------------------------------------------------------")
    def get_page(robot_url):

        response = urllib.request.urlopen(urllib.request.Request(robot_url, headers={'User-Agent': 'Mozilla'}))
        soup = BeautifulSoup(response,'html.parser', from_encoding=response.info().get_param('charset'))
    
        return soup

    robots = get_page(robot_url)
    print(robots)

class Comment():
    arayuz_2()
    secenek = input(colored("Seciminiz: ", 'yellow'))
    print(colored("-----------------------------------------------------------------", 'yellow'))

    try:
        if secenek == '1': # Mevcut sayfayi tara
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            comments = soup.find_all(string=lambda text: isinstance(text, Comment))
            for c in comments:
                print(c)
                print("===========")
                c.extract()

        if secenek == '2': # wayback kullanilacaksa
            waybackpy_url = waybackpy.Url(url, user_agent)
            durum = waybackpy_url.JSON # archive.org da var olup olmadıgının kontrolu
            opt = durum['archived_snapshots']
            #print(durum['archived_snapshots'])
            list = {}
            # print(durum)
            if opt != list: # eger varsa
                arayuz_3()
                print(colored("-----------------------------------------------------------------", 'yellow'))
                wbSecenek = input(colored("Seciminiz: ", 'yellow'))
                print(colored("-----------------------------------------------------------------", 'yellow'))

                if wbSecenek == '1': # en eski URL
                    oldest_archive_url = waybackpy.Url(url, user_agent).oldest()
                    print("-----------------------------------------------------------------")
                    print("Ulasilan en eski URL: ",oldest_archive_url)
                    print("-----------------------------------------------------------------")

                    page = requests.get(oldest_archive_url) # SSL hatasi gelirse:  verify=ssl.CERT_NONE ekle.
                    soup = BeautifulSoup(page.content, 'html.parser')
                    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
                    for c in comments:
                        print(c)
                        print("---------------------------")
                        c.extract()

                if wbSecenek == '2': # en yeni URL
                    newest_archive_url = waybackpy.Url(url, user_agent).newest()
                    print("-----------------------------------------------------------------")
                    print("Ulasilan en yeni URL: ",newest_archive_url)
                    print("-----------------------------------------------------------------")

                    page = requests.get(newest_archive_url)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
                    for c in comments:
                        print(c)
                        print("---------------------------")
                        c.extract()

                if wbSecenek == '3': # yila gore arama yap
                    print(colored("-----------------------------------------------------------------", 'yellow'))
                    year = input(colored("Aranacak Wayback Yili: ", 'yellow'))
                    print(colored("-----------------------------------------------------------------", 'yellow'))
                    target_near = waybackpy_url.near(year)

                    print("-----------------------------------------------------------------")
                    print("Wayback URL:  ", target_near)
                    print("-----------------------------------------------------------------")

                    page = requests.get(target_near)

                    soup = BeautifulSoup(page.content, 'html.parser')

                    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
                    for c in comments:
                        print(c)
                        print("---------------------------")
                        c.extract()

                if wbSecenek == '4':
                    print("-----------------------------------------------------------------")
                    print(colored("Tarihleri girerken rakamlarin basina '0' koymayin! Ornek: 5", 'red'))
                    print("-----------------------------------------------------------------")
                    print(colored("-----------------------------------------------------------------", 'yellow'))
                    year = input(colored("Aranan Wayback Yili: ", 'yellow'))
                    month = input(colored("Ay: ", 'yellow'))
                    day = input(colored("Gun: ", 'yellow'))
                    print(colored("-----------------------------------------------------------------", 'yellow'))
                    target_near = waybackpy_url.near(year, month, day)
                    #print(target_near)
                    print("-----------------------------------------------------------------")
                    print("Wayback URL:  ", target_near)
                    print("-----------------------------------------------------------------")

                    page = requests.get(target_near)
                    soup = BeautifulSoup(page.content, 'html.parser') 

                    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
                    for c in comments:
                        print(c)
                        print("---------------------------")
                        c.extract()

                # else:
                #     print("Hatali secim yaptiniz...")

            else: # eger yoksa
                arayuz_4()
                print(colored("-----------------------------------------------------------------", 'yellow'))
                kayit_secenek = input("Seciminiz: ")
                print(colored("-----------------------------------------------------------------", 'yellow'))

                if kayit_secenek == '1': # su anki halini wb dbsine kaydet.
                    try:
                        archive = waybackpy_url.save() 
                    except WaybackError as e:
                        pass

                    newest_archive_url = waybackpy.Url(url, user_agent).newest()
                    print("-----------------------------------------------------------------")
                    print("Kaydettiginiz URL: ",newest_archive_url)
                    print("-----------------------------------------------------------------")
                    sys.exit()

                if kayit_secenek == '2': # cikis yap
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
