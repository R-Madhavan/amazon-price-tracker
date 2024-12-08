import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6" # https url of the product
sender_email = os.environ["sender_email"]
sender_password = os.environ["sender_password"]
receiver_email = os.environ["receiver_email"]
smpt_address = os.environ["smtp_address"]
target_price = float(910) #set your targe price

# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": "\"Windows\"",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
# }

# minimal headers
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL,headers=header)
soup = BeautifulSoup(response.text,"html.parser")
price = soup.find(class_="aok-offscreen").get_text()
print(price)
price_as_float = float(price.split("$")[1])
print(price_as_float)
title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_as_float < target_price:
    with smtplib.SMTP(smpt_address, 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=f"Subject: Amazon Price Alert! \n\n {title} is on sale for ${price_as_float}\n{URL}".encode("utf-8")
        )
