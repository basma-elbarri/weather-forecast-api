import requests
from datetime import datetime, timedelta



basma = 'author'

is_running = True

while is_running:
    today = datetime.today()



    print("-----------FORECAST----------")
    self = input("Enter your city (n to quit): ").lower()
    temp = input("Celsius(C) or Fahrenheit(F): ").lower()
    if temp == 'f' or temp == 'fahrenheit':
        print('User chose to show temperature in Fahrenheit')
    else:
        print('User chose to show temperature in Celsius')
    days_num = (input("How many days?(between 0-15): "))
    if days_num.isdigit() == False or int(days_num) < 0 or int(days_num) > 15:
        print("Enter a valid number")
        continue

    next_weekday = today + timedelta(days=int(days_num))

    start_date = today.strftime("%Y-%m-%d")
    end_date = next_weekday.strftime("%Y-%m-%d")
    if self == 'n':
        is_running = False
    else:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={self}&count=1&language=en&format=json"

        try:
            response = requests.get(url)
            data = response.json()

        except requests.exceptions.RequestException:
            print("Could not connect to the weather service, please activate your wifi")
            continue


        if "results" not in data:
            print("No results found, enter a valid city")

            continue


        lat = data["results"][0]["latitude"]

        lon = data["results"][0]['longitude']

        name = data["results"][0]["name"]



        web = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        response1 = requests.get(web)
        data1 = response1.json()
        temperature = data1["hourly"]["temperature_2m"]
        humidity = data1["hourly"]["relative_humidity_2m"]
        wind_speed = data1["hourly"]["wind_speed_10m"]
        time = data1["hourly"]["time"]



        index_temp = 0

        def main():
            dati = datetime.today()
            d = -0.5


            index_time = 6
            g = 18
            e = 6
            while g < len(temperature)+12:
                next = dati + timedelta(days=d)
                date_time = datetime.strptime(str(next), "%Y-%m-%d %H:%M:%S.%f")
                if '06:00' in time[index_time]:

                    print(date_time.strftime("%A, %B, %d"), "at day time")

                else:
                    print(date_time.strftime("%A, %B, %d"), "at night time")
                print()
                avg_temp= (sum(temperature[e:g]) / len(temperature[e:g]))
                avg_humidity = (sum(humidity[e:g]) / len(humidity[e:g]))
                avg_windspeed =(sum(wind_speed[e:g]) / len(wind_speed[e:g]))
                if temp == 'f' or temp == 'fahrenheit':
                    far = avg_temp * 1.8 + 32
                    print(f"Temperature: {round(far)}°F ")


                else:
                    print(f"Temperature: {round(avg_temp)}°C ")
                print()
                print(f"Humidity: {round(avg_humidity)}% ")
                print()
                print(f"Wind speed: {round(avg_windspeed)}km/h")
                print('=============================')

                g += 12
                e += 12
                index_time += 12
                d += 0.5


        for i in range(len(temperature)):



            index_temp += 1
        print('---------------------')
        print(f"the forecast in {name}")
        print('---------------------')
        main()