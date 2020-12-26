import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.bestbuy.ca/en-ca/product/samsung-galaxy-note20-ultra-5g-128gb-mystic-bronze-unlocked/14797694'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# these are just place holder's to protect the identity of the creator of this script. Please enter valid details here to make this program work.
sender_email = "senderemail@gmail.com"
sender_password = "sender_password"
reciever_email = "recieveremail@email.com"

def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(
        class_="price_FHDfG large_3aP7Z salePrice_kTFZ3").get_text()[:6] + ".99"
    title = soup.find(class_="productName_19xJx").get_text()

    intprice = price.replace('$', '').replace(',', '')
    intprice = float(intprice)
    if intprice < 2000:
        send_mail(price, title)


def send_mail(price: str, title: str):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sender_email, sender_password)

    subject = "The Price of the Samsung Galaxy Note 20 Ultra on BestBuy!!"

    body = 'Here is the price of the Samsung Galaxy Note 20 Ultra on BestBuy: ' + price + "\nvisit link at:" + URL + "\n\nThank you for using our automated service"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        sender_email,
        reciever_email,
        msg
    )
    server.quit()


if __name__ == "__main__":
    checkPrice()
