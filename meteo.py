import customtkinter as ctk
from PIL import Image
import requests
from weatherapi import *
class app(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='#0F1C2E')
        self.title('Meteo')
        self.geometry('900x500')
        self.resizable(False, False)  #  disable resizing in x and y

        # ===============================
        # VARIABLES
        # ===============================
        self.weather_data = None
        self.check_size = True
        self.entry_var = ctk.StringVar(value ='')
        self.city_var = ctk.StringVar(value='The World')
        self.date_var = ctk.StringVar(value='X X X')
        self.degree_var = ctk.StringVar(value='X°C')
        self.feelslike_var = ctk.StringVar(value='Feelslike:X')
        self.hl_var = ctk.StringVar(value='H: X°C L: X°C')
        self.condition_var = ctk.StringVar(value='Condition: X')
        self.humidity_var = ctk.StringVar(value='Humidity: X')
        self.wind_var = ctk.StringVar(value='Wind: X')
        self.uv_var = ctk.StringVar(value='UV Index: X')
        self.pressure_var = ctk.StringVar(value='Pressure: X')
        self.visibility_var = ctk.StringVar(value='Visibility: X')
        # icon image:
        self.condition_name = 'theworld'
        self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100)
        )

        # ===============================
        # WIDGETS
        # ===============================
        self.widgets()
        self.mainloop()

    def widgets(self):
        self.entry = EntryFrame(self)
        self.EntryFrameWidgets()
        self.main = MainFrame(self)
        self.MainFrameWidgets()

    def EntryFrameWidgets(self):
        # ---------- Left: City + Date ----------
        frame1 = ctk.CTkFrame(self.entry, fg_color='transparent', corner_radius=0)

        self.label_city = ctk.CTkLabel(
            frame1,
            textvariable=self.city_var,
            font=ctk.CTkFont("arial", 50, "bold")
        )
        self.label_city.pack(anchor="nw", padx=10)

        label_date = ctk.CTkLabel(
            frame1,
            textvariable=self.date_var,
            font=ctk.CTkFont("arial", 15)
        )
        label_date.pack(anchor="nw", padx=10)

        frame1.pack(side='left', expand=True, fill='both', pady=15)

        # ---------- Right: Search ----------
        frame2 = ctk.CTkFrame(self.entry, fg_color='transparent', corner_radius=0)
        frame3 = ctk.CTkFrame(frame2, fg_color='transparent', corner_radius=0)
        frame3.pack(side='right', expand=True, fill='both')
        resize_image = ctk.CTkImage(
                light_image = Image.open('images/meteoapp/shrink.png'),
                dark_image = Image.open('images/meteoapp/shrink.png')
            )
        resize = ctk.CTkButton(
                master = frame2,
                text = '',
                image = resize_image,
                fg_color = 'transparent',
                hover_color = '#0F1C2E',
                width = 10,
                cursor = 'hand2',
                command = lambda : self.resize_window()

            )
        resize.place(relx = 0.95,rely = 0.2,anchor = 'center')
        entry = ctk.CTkEntry(
            frame3,
            corner_radius=20,
            width=200,
            height=35,
            textvariable=self.entry_var,
            fg_color='transparent',
            placeholder_text='⌕ search a city '
        )
        entry.pack(side='left', expand=True, fill='x')
        entry.bind('<FocusOut>', lambda event: entry.configure(placeholder_text=' search a city'))

        searchbutton = ctk.CTkButton(
            frame3,
            corner_radius=20,
            text='search',
            width=60,
            height=35,
            font = ctk.CTkFont('arial',12,'bold'),
            cursor = 'hand2',
            fg_color='#4459ad',
            command = lambda : self.get_weather()
        )
        searchbutton.pack(side='left', expand=True)
        frame2.pack(side='right', expand=True, fill='both')

    def MainFrameWidgets(self):
        # ---------- Left Panel ----------
        frame1 = ctk.CTkFrame(self.main, corner_radius=15, fg_color='#4f596e')

        # Weather icon
        icon = self.icon_image
        self.icon_label =ctk.CTkLabel(
            frame1,
            text='',
            image=icon
        )
        self.icon_label.pack(pady=10)

        # Temperature
        ctk.CTkLabel(
            frame1,
            textvariable=self.degree_var,
            font=ctk.CTkFont('Helvetica', 140, 'bold')
        ).pack(pady=10)

        # Feels like + High/Low
        feelslikeframe = ctk.CTkFrame(frame1, fg_color='transparent')
        Font = ctk.CTkFont('arial', 20)

        ctk.CTkLabel(
            feelslikeframe,
            textvariable=self.feelslike_var,
            font=Font
        ).pack(side='left', padx=20)

        ctk.CTkLabel(
            feelslikeframe,
            textvariable=self.hl_var,
            font=Font
        ).pack(side='right', padx=20)

        feelslikeframe.pack(fill='x')
        frame1.pack(side='left', expand=True, fill='both', padx=15, pady=15)

        # ---------- Right Panel ----------
        frame2 = ctk.CTkFrame(self.main, fg_color='#4f596e', corner_radius=15)
        Font = ctk.CTkFont('arial', 18)

        # Condition
        label_condition = ctk.CTkLabel(
            frame2,
            textvariable=self.condition_var,
            font=ctk.CTkFont('arial', 22, 'bold')
        )
        label_condition.pack(anchor='nw', padx=20, pady=(20, 5))

        # Humidity
        label_humidity = ctk.CTkLabel(
            frame2,
            textvariable=self.humidity_var,
            font=Font
        )
        label_humidity.pack(anchor='nw', padx=20, pady=10)

        # Wind
        label_wind = ctk.CTkLabel(
            frame2,
            textvariable=self.wind_var,
            font=Font
        )
        label_wind.pack(anchor='nw', padx=20, pady=10)

        # UV Index
        label_uv_title = ctk.CTkLabel(
            frame2,
            text="UV Index",
            font=ctk.CTkFont('arial', 20, 'bold')
        )
        label_uv_title.pack(anchor='nw', padx=20, pady=(10, 2))

        label_uv_value = ctk.CTkLabel(
            frame2,
            textvariable=self.uv_var,
            font=Font
        )
        label_uv_value.pack(anchor='nw', padx=20, pady=10)

        # Pressure
        label_pressure = ctk.CTkLabel(
            frame2,
            textvariable=self.pressure_var,
            font=Font
        )
        label_pressure.pack(anchor='nw', padx=20, pady=10)

        # Visibility
        label_visibility = ctk.CTkLabel(
            frame2,
            textvariable=self.visibility_var,
            font=Font
        )
        label_visibility.pack(anchor='nw', padx=20, pady=10)

        frame2.pack(side='left', expand=True, fill='both', padx=15, pady=15)
    def get_weather(self):
        user_input = self.entry_var.get()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_id}"
        print("Requesting:", url)
        try:
            response = requests.get(url,timeout =5)
            weather_data = response.json()
        except Exception as e :
            # making icon 
            poorconnection = ctk.CTkImage(
                light_image = Image.open('images/meteoapp/no-signal.png'),
                dark_image = Image.open('images/meteoapp/no-signal.png'),
                size =(50,50)
            )
            self.notification('Poor connection\nTry again',poorconnection)
            return

        if str(weather_data.get("cod")) == "404":
                nocity = ctk.CTkImage(
                light_image = Image.open('images/meteoapp/no-results.png'),
                dark_image = Image.open('images/meteoapp/no-results.png'),
                size =(50,50))

                self.notification('No city founded\nTry again',nocity)
        else:
            self.weather_data  = weather_data
            self.set_weather()
    def set_weather(self):
        if not self.weather_data:
            return
        
        data = self.weather_data
        condition = data['weather'][0]['id']
        self.get_condition(condition)
        # ===============================
        # MAIN INFO
        # ===============================
        city_name = self.entry_var.get().title()
        country = data["sys"]["country"]
        temp = round(data["main"]["temp"])
        feels_like = round(data["main"]["feels_like"])
        temp_min = round(data["main"]["temp_min"])
        temp_max = round(data["main"]["temp_max"])
        condition = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        visibility = data.get("visibility", 0) / 1000  # convert meters → km

        # ===============================
        # SET VARIABLES
        # ===============================
        self.city_var.set(f"{city_name}, {country}")
        self.update_font()
        # (you can format date using datetime if you want real date)
        from datetime import datetime
        self.date_var.set(datetime.now().strftime("%A, %b %d"))

        self.degree_var.set(f"{temp}°C")
        self.feelslike_var.set(f"Feels like: {feels_like}°C")
        self.hl_var.set(f"H: {temp_max}°C  L: {temp_min}°C")

        self.condition_var.set(condition)

        self.humidity_var.set(f"Humidity: {humidity}%")
        self.wind_var.set(f"Wind: {wind_speed} m/s")
        self.uv_var.set("UV Index: N/A")   # 
        self.pressure_var.set(f"Pressure: {pressure} hPa")
        self.visibility_var.set(f"Visibility: {visibility:.1f} km")
        print(self.condition_name)
    def get_condition(self,cond):
        if 200<= cond <=232:
            self.condition_name = 'thunderstorm' 
            self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100)
            )
            self.icon_label.configure(image = self.icon_image)
        elif 300<= cond <=321:
            self.condition_name = 'drizzle' 
            self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100))
            self.icon_label.configure(image = self.icon_image)
        elif 500<= cond <=531:
            self.condition_name = 'rain'
            self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100))
            self.icon_label.configure(image = self.icon_image) 
        elif 600<= cond <=622:
            self.condition_name = 'snowy'
            self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100))
            self.icon_label.configure(image = self.icon_image) 
        elif 701<= cond <=741:
            self.condition_name = 'fog' 
            self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100))
            self.icon_label.configure(image = self.icon_image)
        elif cond ==762:
            self.condition_name = 'ash' 
            self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100))
            self.icon_label.configure(image = self.icon_image) 
        elif cond ==771:
            self.condition_name = 'squall'
            self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100))
            self.icon_label.configure(image = self.icon_image) 
        elif cond ==781:
            self.condition_name = 'tornado' 
            self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100))
            self.icon_label.configure(image = self.icon_image)
        elif cond ==800:
            self.condition_name = 'cloudy-day'
            self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100))
            self.icon_label.configure(image = self.icon_image) 
        elif 801<= cond <=804:
            self.condition_name = 'clouds' 
            self.icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            dark_image=Image.open(f'images/meteoapp/{self.condition_name}.png'),
            size=(100, 100))
            self.icon_label.configure(image = self.icon_image)
    def resize_window(self):
        if self.check_size:
            self.check_size = False
            self.entry.destroy()
            self.main.destroy()
            self.geometry('300x400')
            self.small_app()
        else:
            self.check_size = True
            self.parent_frame.destroy()
            self.geometry('900x500')
            self.widgets()

    def small_app(self):
        self.resizable(False,False)
        # search bar and button
        self.parent_frame = ctk.CTkFrame(self,fg_color ='transparent',corner_radius=0)
        frame1 = ctk.CTkFrame(self.parent_frame,fg_color ='transparent',corner_radius = 0)
        # frame widgets 
        frameentry = ctk.CTkFrame(frame1,fg_color = 'transparent',corner_radius = 0)
        smallentry = ctk.CTkEntry(
                frameentry,
                corner_radius = 20,
                height=35,
                width =200 ,
                textvariable=self.entry_var,
                fg_color='transparent',
                placeholder_text='⌕ search a city '
            )
        smallentry.pack(pady = 5)

        resize_image = ctk.CTkImage(
                light_image = Image.open('images/meteoapp/bigger.png'),
                dark_image = Image.open('images/meteoapp/bigger.png')
            )
        resize = ctk.CTkButton(
                master = frameentry,
                text = '',
                image = resize_image,
                fg_color = 'transparent',
                hover_color = '#0F1C2E',
                width = 10,
                cursor = 'hand2',
                command = lambda: self.resize_window()

            )
        resize.place(relx = 0.93,rely = 0.5,anchor = 'center')
        frameentry.pack(fill = 'x')
        smallsearchbutton = ctk.CTkButton(
                    frame1,
                    corner_radius=20,
                    text='search',
                    width=60,
                    height=35,
                    font = ctk.CTkFont('arial',12,'bold'),
                    cursor = 'hand2',
                    fg_color='#4459ad',
                    command = lambda : [self.get_weather(),self.update_font()]
            )
        smallsearchbutton.pack(pady = 10)
        frame1.pack(fill = 'x')
        frame2 = ctk.CTkFrame(self.parent_frame,fg_color ='transparent',corner_radius = 0)
        # degree
        ctk.CTkLabel(
                    frame2,
                    textvariable=self.degree_var,
                    font=ctk.CTkFont('Helvetica', 70, 'bold')
                ).pack(pady=10)

        icon = self.icon_image
        self.icon_label =ctk.CTkLabel(
                    frame2,
                    text='',
                    image=icon
                )
        self.icon_label.pack(pady=10)
        self.label_condition = ctk.CTkLabel(
                    frame2,
                    textvariable=self.condition_var,
                    font= ctk.CTkFont('arial',30,'bold')

                )
        self.label_condition.pack(padx=20, pady=15)
        frame2.pack(fill = 'x')
        self.parent_frame.pack(fill ='x')
    def update_font(self):
        if not self.check_size:
            if len(self.condition_var.get())>15:
                Font = ctk.CTkFont('arial',15,'bold')
                self.label_condition.configure(font =Font)
            else:
                Font = ctk.CTkFont('arial',30,'bold')
                self.label_condition.configure(font =Font)
        else:
            city_name = self.city_var.get()
            if len(city_name) > 15 : 
                self.label_city.configure(font =ctk.CTkFont('arial',30,'bold'))
            else:
                self.label_city.configure(font =ctk.CTkFont('arial',50,'bold'))
    def notification(self,text,image):
        toplevel = ctk.CTkToplevel(fg_color = '#0F1C24')
        toplevel.wm_attributes("-transparentcolor", "#0F1C24")
        toplevel.overrideredirect(True)  # hides title bar (including X and -)
        topframe = ctk.CTkFrame(toplevel,fg_color = '#0F1C2E',corner_radius = 20)
        Font = ctk.CTkFont('Helvetica',18,'bold')
        ctk.CTkLabel(master=topframe,text = text,text_color = 'white',font = Font ,fg_color = 'transparent',image = image,compound ='top').pack(pady =10,padx =20)
        self.eval(f'tk::PlaceWindow {str(toplevel)} center')
        ctk.CTkButton(topframe,
            text = 'close',
            font = Font ,
            command = lambda : [toplevel.destroy()],
            width = 100,
            height = 30,
            fg_color = 'red'
            ).pack(pady = 10)
        topframe.pack(expand = 'True',fill = 'both')
class EntryFrame(ctk.CTkFrame):
    def __init__(self, parent, fg_color='transparent'):
        super().__init__(
            master=parent,
            fg_color=fg_color,
            corner_radius=0,
        )
        self.place(relx=0, rely=0, relheight=0.2, relwidth=1)


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, fg_color='#0F1C2E'):
        super().__init__(
            master=parent,
            fg_color=fg_color
        )
        self.place(relx=0, rely=0.20, relheight=0.8, relwidth=1)


if __name__ == '__main__':
    app()

