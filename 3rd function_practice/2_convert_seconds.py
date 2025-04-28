def convert_seconds(time):
    hours = time // 3600
    minutes = time % 3600 // 60
    print(f'В {time} секундах содержится {hours} час(ов) и {minutes} минут(ы)')

convert_seconds(4532400)