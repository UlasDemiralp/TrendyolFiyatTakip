from wsgiref import headers
import requests  
from bs4 import BeautifulSoup 
from send_email import sendMail
import time


url1="https://www.trendyol.com/miababy/pamuk-bereli-3-lu-takim-bebek-ve-cocuk-nefti-yesil-p-445482731?boutiqueId=673982&merchantId=686349&sav=true"



def checkPrice(url,paramPrice):

    headers={
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

    }   


    page = requests.get(url, headers=headers)

    htmlpage =BeautifulSoup(page.content,'html.parser')


    productTitle=htmlpage.find("h1", class_="pr-new-br" ).getText()

    price = htmlpage.find("span", class_="prc-dsc").getText()

    image = htmlpage.find("img",class_="base-product-image")

    print(productTitle)

    convertedPrice = float(price.replace(".", "").replace(",", ".").replace("TL", "").strip())

    if(convertedPrice>=paramPrice):

        print ("Ürünün fiyatı Düştü")
        htmlEmailContent= """\
        <html>
        <head></head>
        <body>
        <h3>{0}</h3>
        <br/>
        {1}
        <br/> Ürün linki:{2}</p>
        </body>
        </html>

        """.format(productTitle,image,url)
        sendMail("ulasdemiralp2004@gmail.com","Ürünün Fiyatı Düştü", htmlEmailContent)
        print (convertedPrice)
    else:
        print("Fiyat düşmedi")

istek = True

while (istek):
    checkPrice(url1,300)
    time.sleep(3)
    istek = False