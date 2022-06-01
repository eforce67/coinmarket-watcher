from ast import arguments
import time, pytz, prices, os
from datetime import datetime
from pathlib import Path


def update_Time(coin, timezone):
    loop = 0
    loop_second = 0
    timestart_price = []

    # creating a datasheet
    path = str(os.path.join(Path.home(), "Downloads\CoinMarket_sheets"))
    now = datetime.now()
    date = now.strftime("%d/%m/%Y_%H:%M:%S")
    date1 = date.replace(":", "-")
    date2 = date1.replace("/", "-")

    # creating the folder to downloads if the path does not exist
    if not os.path.exists(path):
        os.makedirs(path)

    with open(f"{path}\{coin}_{date2}" + ".txt", "w+") as file:
        print(f"a filed called {coin}_{date2} has been created for this session")
        file.close()

    time.sleep(1.5)

    while True:
        time.sleep(1.5)
        os.system("cls||clear")

        am_pm = ""
        timezones = pytz.timezone(timezone)

        time.sleep(1)
        datetime_NY = datetime.now(timezones)

        if int(datetime_NY.strftime("%H")) > 12:
            am_pm = "pm"
        elif int(datetime_NY.strftime("%H")) < 12:
            am_pm = "am"

        price_bal = prices.get_current_Price(coin)
        current_time = str(datetime_NY.strftime("%H:%M:%S")) + am_pm

        loop += 1
        loop_second += 1
        if loop == 1:
            current_time_start = str(datetime_NY.strftime("%H:%M:%S") + am_pm)
            timestart_price.append(str(price_bal) + " -TIME: " + current_time_start)

        # credits to geeksforgeeks.org i can't do math sorry
        # https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/

        """
        seconds = loop_second % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        total_time = "%d:%02d:%02d" % (hour, minutes, seconds)
        """

        datafile = open(f"{path}\{coin}_{date2}" + ".txt", "r+", encoding="utf-8")
        datafile.write(
            f"""[LOOP {loop}] current price when the machine ran: {timestart_price} | {timezone} time: {current_time} | {coin} price: {price_bal}\n"""
        )
        print(
            f"""
              current price when the machine ran: {timestart_price}
              {timezone} time: {current_time}
              
              {coin} price: {price_bal}"""
        )
        total_time = loop * 3600

        print(f"please wait 1 hour | up-time: {total_time} seconds")
        time.sleep(3597.5)
