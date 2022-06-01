from bs4 import BeautifulSoup
import requests, re


def get_current_Price(coin):
    website = requests.get(f"https://coinmarketcap.com/currencies/{coin}/")
    soup = BeautifulSoup(website.content, "html.parser")

    volume_arrow = ""

    find_content = soup.find_all("div", {"class": "priceValue"})
    volume_price = soup.find("span", {"class": "sc-15yy2pl-0 feeyND"})
    volume_price1 = soup.find("span", {"class": "sc-15yy2pl-0 gEePkg"})

    if "icon-Caret-down" in str(volume_price):
        volume_arrow = "➘ -down"
        vol = str(volume_price)[125:]
        vol = re.sub("\D", "", vol)

    elif "icon-Caret-up" in str(volume_price1):
        volume_arrow = "➚ -up"
        vol = str(volume_price1)[125:]
        vol = re.sub("\D", "", vol)
    else:
        volume_arrow == "unknown volume"

    for items in find_content:
        for letters in items:
            for number in letters:
                num = number
                # 1.00
                if len(vol) == 3:
                    volx = vol[:1] + "." + vol[1:]
                # 10.00
                elif len(vol) == 4:
                    volx = vol[:2] + "." + vol[2:]
                # 100.00
                elif len(vol) == 5:
                    volx = vol[:3] + "." + vol[3:]
                # 1000.00
                elif len(vol) == 6:
                    volx = vol[:4] + "." + vol[4:]
                # 10.000
                elif len(vol) == 7:
                    volx = vol[:5] + "." + vol[5:]

                else:
                    # debugging purposes
                    volx = "unknown length"
    try:
        return str(num + " " + volume_arrow + " " + volx + "%")

    except UnboundLocalError:
        return "there was a error in finding that coin/token"
