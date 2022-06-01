# Program by Neonsharp
# coinmarket price tracker

# made without api

# finished 8:40pm, 3/4/2022

import updater, time, pytz, sys


def main():
    coin = input("enter a coin: ")
    coin.lower

    for timez in pytz.all_timezones:
        print(timez)

    print("TIPS: make sure what you enter matches the list")

    try:
        timezone = input("enter your country: ")
    except KeyboardInterrupt:
        print("please watch out for any typo")
        timezone = input("enter your country: ")

    time.sleep(1)
    print(
        f"""
          the coin you enter was {coin}
          the timezone you enter was {timezone}"""
    )

    # lazy developer moment but if it works it works ;---;
    try:
        updater.update_Time(coin, timezone)
    except UnboundLocalError or pytz.exceptions.UnknownTimeZoneError:
        try:
            print("please make sure your typing without any typo")
            timezone = input("enter your country: ")
        except KeyboardInterrupt:
            print("please watch out for any typo")
            timezone = input("enter your country: ")


if __name__ == "__main__":
    main()
