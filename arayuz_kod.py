from termcolor import colored

def arayuz_1():
    print(colored("-----------------------------------------------------------------", 'green'))
    print(colored("Scrape & Parse Islemleri",'green'))
    print(colored("-----------------------------------------------------------------", 'green'))

def arayuz_2():
    print(colored("-----------------------------------------------------------------", 'green'))
    print(colored("Yorum Satırları Tarama Islemleri", 'green' ))
    print(colored("-----------------------------------------------------------------", 'green'))
    print("-----------------------------------------------------------------")
    print("Guncel web sayfasi taramak icin - 1")
    print("Wayback Machine kullanmak icin - 2")
    print("-----------------------------------------------------------------")
    print(colored("-----------------------------------------------------------------", 'yellow'))

def arayuz_3():
    print("-----------------------------------------------------------------")
    print("Wayback Machinede bulunan en eski sayfaya ulasmak icin - 1")
    print("Wayback Machinede bulunan en yeni sayfaya ulasmak icin - 2")
    print("Wayback Machinede istediginiz yila ait sayfaya ulasmak icin - 3")
    print("Wayback Machinede belirli bir tarihe ait sayfaya ulasmak icin - 4")
    print("-----------------------------------------------------------------")

def arayuz_4():
    print("-----------------------------------------------------------------")
    print("Aradiginiz sayfa icin Wayback Machine'de veri bulunamadi.")
    print("Aradiginiz sayfayi archive.org'a kaydetmek icin - 1")
    print("Cikis yapmak icin - 2")
    print("-----------------------------------------------------------------")