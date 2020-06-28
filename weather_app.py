import requests
import json
from tkinter import *
import datetime 
import calendar
from PIL import Image,ImageTk
from pprint import pprint 
root = Tk()
root.title('Weather App')
root.geometry('560x400')
root.iconbitmap('weather.ico')
root.maxsize(560,400)
root.minsize(560,400)

# weather app text
weather_app = Label(root,text="WEATHER APP",font=("Times", "24", "bold italic"),bg='#87ceeb',pady=5)
weather_app.pack()
weather_img=[]
# downloading weather condition image
def get_image(url_img,image_name):
    global weather_img
    url = requests.get(f'http:{url_img}')
    with open(image_name,'wb') as f:
        f.write(url.content)
    f.close()
    weather_img.append(ImageTk.PhotoImage(Image.open(image_name)))

three_days=[]
def three_day_list(three_day):
    t_day = datetime.datetime.strptime(three_day, '%Y-%m-%d').weekday()
    three_days.append(calendar.day_name[t_day][:3])
    
# request of weather
def weather_request(location):
    url=requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=7b54a7820ee14ca593580859200105&q={location}&days=7')
    data = url.json()
    return data['location']['name'],data['location']['region'],data['location']['country'],data['current']['temp_c'],data['current']['temp_f'],data['current']['condition']['text'],data['current']['wind_mph'],data['current']['wind_kph'],data['current']['wind_degree'],data['current']['wind_dir'],data['current']['pressure_mb'],data['current']['humidity'],data['current']['condition']['icon'],data['forecast']


# get location text
def get_location(event):
    try:
        weather_img.clear()
        three_days.clear()
        name,region,country,temp_c,temp_f,condtion,wind_mph,wind_kph,wid_deg,wind_dir,pressure_mb,humd,today_weather_img,all_three_days_data= weather_request(location_text.get())

        # get image of weather
        get_image(today_weather_img,'today_weather.png')
        get_image(all_three_days_data['forecastday'][1]['day']['condition']['icon'],'today_weather2.png')
        get_image(all_three_days_data['forecastday'][2]['day']['condition']['icon'],'today_weather3.png')
        # three days list
        three_day_list(all_three_days_data['forecastday'][0]['date'])
        three_day_list(all_three_days_data['forecastday'][1]['date'])
        three_day_list(all_three_days_data['forecastday'][2]['date'])
        
        # updating the label value
        location.update()
        daytime.update()
        weather_condition.update()
        temperature.update()
        degree_celcius.update()
        pressure.update()
        humidity.update()
        wind.update()
        
        # set the label text
        weather_condition_image.config(image=weather_img[0])
        location_string.set(f'{name},{region}')
        daytime_string.set(f'{day} {time}')
        weather_condition_string.set(condtion)
        temperature_string.set(int(temp_c))
        degree_celcius_string.set("°C")
        pressure_string.set(f'Pressure: {int(pressure_mb)}hpa')
        humidity_string.set(f'Humidity: {humd}%')
        wind_string.set(f'Wind: {int(wind_kph)} km/h')
        location_text.delete(0,END)
        
        # first days work update
        first_day.update()
        first_day_temp.update()
        
        # second days work update
        second_day.update()
        second_day_temp.update()
        
        # third days work update
        third_day.update()
        third_day_temp.update()
        
        # first day string set

        first_daytime_string.set(three_days[0])
        first_temperature_string.set(f"{int(all_three_days_data['forecastday'][0]['day']['avgtemp_c'])}°C to {int(all_three_days_data['forecastday'][0]['day']['maxtemp_c'])}°C , {int(all_three_days_data['forecastday'][0]['day']['avghumidity'])}%")
        first_day_image.config(image=weather_img[0])

        # second day string set

        second_daytime_string.set(three_days[1])
        second_temperature_string.set(f"{int(all_three_days_data['forecastday'][1]['day']['avgtemp_c'])}°C to {int(all_three_days_data['forecastday'][1]['day']['maxtemp_c'])}°C , {int(all_three_days_data['forecastday'][1]['day']['avghumidity'])}%")
        second_day_image.config(image=weather_img[1])
        
        # third day string set

        third_daytime_string.set(three_days[2])
        third_temperature_string.set(f"{int(all_three_days_data['forecastday'][2]['day']['avgtemp_c'])}°C to {int(all_three_days_data['forecastday'][2]['day']['maxtemp_c'])}°C , {int(all_three_days_data['forecastday'][2]['day']['avghumidity'])}%")
        third_day_image.config(image=weather_img[2])
    except Exception as e:
        print(e)

# day date and time function
def timedateday():
    today = datetime.datetime.now()
    date_month_year = today.strftime("%d %m %Y")
    day = datetime.datetime.strptime(date_month_year, '%d %m %Y').weekday()
    time =today.strftime("%I:%M %p")
    return calendar.day_name[day],date_month_year,time

# day date and time are defined
day,date,time=timedateday() 
    
# all string
location_string = StringVar()
daytime_string = StringVar()
weather_condition_string = StringVar()
temperature_string = StringVar()
degree_celcius_string=StringVar()
pressure_string=StringVar()
humidity_string = StringVar()
wind_string = StringVar()

# first day string

first_daytime_string = StringVar()
first_temperature_string = StringVar()

# second day string

second_daytime_string = StringVar()
second_temperature_string = StringVar()

# third day string

third_daytime_string = StringVar()
third_temperature_string = StringVar()


# all string set

location_string.set("")
daytime_string.set("")
weather_condition_string.set("")
temperature_string.set("")
degree_celcius_string.set("")
pressure_string.set("")
humidity_string.set("")
wind_string.set("")

# first day string set

first_daytime_string.set("")
first_temperature_string.set("")

# second day string set

second_daytime_string.set("")
second_temperature_string.set("")

# third day string set

third_daytime_string.set("")
third_temperature_string.set("")


# location entry box 
location_text = Entry(root,font=("Arial", "20"),width=30,borderwidth=2)
location_text.bind('<Return>',get_location)
location_text.place(x=50,y=50)

# location
location = Label(root,textvariable=location_string,font=("pacifico", "20","italic"),bg='#87ceeb')
location.place(x=10,y=100)

# daytime
daytime = Label(root,textvariable=daytime_string,font=("Times", "14","italic"),bg='#87ceeb')
daytime.place(x=10,y=135)

#weather condition
weather_condition=Label(root,textvariable=weather_condition_string,font=("Times", "14","italic"),bg='#87ceeb')
weather_condition.place(x=10,y=160)

#weather condition image
weather_condition_image=Label(root,bg='#87ceeb')
weather_condition_image.place(x=20,y=185)

# temperature
temperature=Label(root,textvariable=temperature_string,font=("Times", "40","italic"),bg='#87ceeb')
temperature.place(x=100,y=185)

# degree_celcius
degree_celcius=Label(root,textvariable=degree_celcius_string,font=("Times", "14","italic"),bg='#87ceeb')
degree_celcius.place(x=160,y=190)

# pressure
pressure=Label(root,textvariable=pressure_string,font=("Times", "14","italic"),bg='#87ceeb')
pressure.place(x=350,y=180)

# humidity
humidity=Label(root,textvariable=humidity_string,font=("Times", "14","italic"),bg='#87ceeb')
humidity.place(x=350,y=207)

# wind
wind=Label(root,textvariable=wind_string,font=("Times", "14","italic"),bg='#87ceeb')
wind.place(x=350,y=234)

# first day work

first_day_my_canvas= Canvas(root,width=150,height=120,bg='#87ceeb')
first_day_my_canvas.place(x=50,y=270)

first_day=Label(root,textvariable=first_daytime_string,font=("Times", "12","italic bold"),bg='#87ceeb')
first_day.place(x=110,y=275)

first_day_image=Label(root,bg='#87ceeb')
first_day_image.place(x=92,y=295)

first_day_temp=Label(root,textvariable=first_temperature_string,font=("Times", "12","italic bold"),bg='#87ceeb')
first_day_temp.place(x=60,y=365)


# second day work

second_day_my_canvas= Canvas(root,width=150,height=120,bg='#87ceeb')
second_day_my_canvas.place(x=50+150,y=270)

second_day=Label(root,textvariable=second_daytime_string,font=("Times", "12","italic bold"),bg='#87ceeb')
second_day.place(x=110+150,y=275)

second_day_image=Label(root,bg='#87ceeb')
second_day_image.place(x=92+150,y=295)

second_day_temp=Label(root,textvariable=second_temperature_string,font=("Times", "12","italic bold"),bg='#87ceeb')
second_day_temp.place(x=60+150,y=365)


# third day work

third_day_my_canvas= Canvas(root,width=150,height=120,bg='#87ceeb')
third_day_my_canvas.place(x=50+150+150,y=270)

third_day=Label(root,textvariable=third_daytime_string,font=("Times", "12","italic bold"),bg='#87ceeb')
third_day.place(x=110+150+150,y=275)

third_day_image=Label(root,bg='#87ceeb')
third_day_image.place(x=92+150+150,y=295)

third_day_temp=Label(root,textvariable=third_temperature_string,font=("Times", "12","italic bold"),bg='#87ceeb')
third_day_temp.place(x=60+150+150,y=365)

# loop ends
root.configure(bg='#87ceeb')
root.mainloop()
 
##  '20°C to 30°C , 50%'
