import requests
import bs4



html = requests.get("https://www.legendww.me/zenska-odjeca")

def pridobi_ime(blok):
    ime=blok.find_all("div",attrs={"class":"product__teaser__title"})
    return ime.h2.string
    
def pridobi_ceno(blok):
    podatki=blok.find_all("div",attrs={"class":"product__teaser__price"})
    ceno=float(ime.div.span)
    valuta= podatki.div.next.next_sibling.next_sibling.next_sibling 
    return ceno,valuta

juha = bs4.BeautifulSoup(html.content)

with open("podatki\oblacila.csv","w", encoding="UTF-8") as dat:
    print("ime,cena,valuta",file=dat)
    for izdelek in juha.find_all("div",attrs={"class":"product__teaser"}):
        ime=pridobi_ime(izdelek)
        cena, valuta=pridobi_ceno(izdelek)
        
        print(f"{ime},{cena},{valuta}",file=dat)
    

    


