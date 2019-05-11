import json
from arrays import Array


class SkiWeather:
    """Class for weather conditions' representation"""
    def __init__(self, data):
        """Initialization a new instance of the class"""
        self.data = data
        self.named = [x for x in self.data][0]
        

    def if_error(self):
        """Check if there are some weather data"""
        if "error" in [x for x in self.data[self.named]["data"]]:
            return True
        return False

    def get_request(self):
        if not self.if_error():
            return [x for x in self.data[self.named]["data"]["request"]][0]
        else:
            return None
    
    def name(self):
        """Return a location`s name"""
        req = self.get_request()
        if req is not None:
            return req["query"]
        return req

    def get_weather(self):
        """(SkiWeather) -> list 
        Return all weather conditions"""
        if not self.if_error():
            n = [x for x in self.data[self.named]["data"]["weather"]]
            return n
        else:
            return None
        
    def totalSnowfall_cm(self):
        """(SkiWeather) -> list 
        Return total expected snowfall in a day"""
        weather = self.get_weather()
        if weather is None:
            return None
        return [int(float(wea["totalSnowfall_cm"])) for wea in weather]
           
           
    def chanceofsnow(self):
        """(SkiWeather) -> list 
        Return chance of snow in a day"""
        weather = self.get_weather()
        if weather is None:
            return None
        return [int(float(wea["chanceofsnow"])) for wea in weather]


    def hourly(self):
        """(SkiWeather) -> list 
        Return information about the weather forecast for the hour."""
        weather = self.get_weather()
        if weather is None:
            return None
        return [wea["hourly"] for wea in weather]


    def chanceoffog(self):
        """(SkiWeather) -> list(int, ...)
        Return a chance of fog"""
        hourly = self.hourly()
        if hourly is None:
            return None
        return [int(conditions["chanceoffog"]) for conditions in hourly[0]]

    def chanceofthunder(self):
        """(SkiWeather) -> list(int, ...)
        Return a chance of thunder"""
        hourly = self.hourly()
        if hourly is None:
            return None
        return [int(conditions["chanceofthunder"]) for conditions in hourly[0]]

    
    def chanceofwindy(self):
        """(SkiWeather) -> list(int, ...)
        Return a chance windy"""
        hourly = self.hourly()
        if hourly is None:
            return None
        return [int(conditions["chanceofwindy"]) for conditions in hourly[0]]

    def snowfall_cm(self):
        """(SkiWeather) -> list(int, ...)
        Return a chance of snowfall"""
        hourly = self.hourly()
        if hourly is None:
            return None
        return [int(float(conditions["snowfall_cm"])) for conditions in hourly[0]]


    def visibility(self):
        """(SkiWeather) -> list(int, ...)
        Return a Visibility in kilometers"""
        hourly = self.hourly()
        if hourly is None:
            return None
        return [int(conditions["visibility"]) for conditions in hourly[0]]


    def chanceofrain(self):
        """(SkiWeather) -> list(int, ...)
        Return a chance"""
        hourly = self.hourly()
        if hourly is None:
            return None
        return [int(conditions["chanceofrain"]) for conditions in hourly[0]]


    def date(self):
        """(SkiWeather) -> list(string, ...) 
        Return local forecast date"""
        weather = self.get_weather()
        if weather is None:
            return None
        return [wea["date"] for wea in weather]


    def bottom_min(self):
        """(SkiWeather) -> list(int, ...)"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["bottom"][0]
            res.append(int(wea_['maxtempC']))
        return res


    def bottom_max(self):
        """(SkiWeather) -> list(int, ...)"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["bottom"][0]
            res.append(int(wea_['mintempC']))
        return res

    def mid_min(self):
        """(SkiWeather) -> list(int, ...)"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["mid"][0]
            res.append(int(wea_['maxtempC']))
        return res


    def mid_max(self):
        """(SkiWeather) -> list(int, ...)"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["mid"][0]
            res.append(int(wea_['mintempC']))
        return res


    def top_min(self):
        """(SkiWeather) -> list(int, ...)"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["top"][0]
            res.append(int(wea_['maxtempC']))
        return res
        
    def top_max(self):
        """(SkiWeather) -> list(int, ...)"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["top"][0]
            res.append(int(wea_['mintempC']))
        return res
    
    def __str__(self):
        return str(self.name())
 
    def whether(self):
        """(SkiWeather) -> list(bool, ...)"""
        # Визначає чи погода оптимальна для лещетарства 
        if self.totalSnowfall_cm()[0] == 30 or\
            self.chanceofsnow()[0] <= 10:
            return [False] * 3
        if (self.bottom_min()[0] > 8 or\
            self.mid_min()[0] > 8 or\
            self.top_min()[0] > 8)\
            or\
            (self.bottom_max()[0] < 2 or\
            self.mid_max()[0] < 2 or\
            self.top_max()[0] < 2):
            return [False] * 3
        lst = [False] * 4    
        for i in range(4):
            if self.chanceoffog()[i] < 50:
                lst[i] = True
            if self.chanceofthunder()[i] < 50:
                lst[i] = True
            if self.chanceofrain()[i] < 30:
                lst[i] = True
            if self.snowfall_cm()[i] > 0:
                lst[i] = True
            if self.visibility()[i] > 1:
                lst[i] = True
        return lst[1:]

            



# if __name__ == "__main__":
#     f = open('data.json', encoding = 'utf-8')
#     all_data = json.load(f)

#     ski_list = list(key for key in all_data['resorts'])
#     resorts_list = Array(len(ski_list))
    
#     for i in range(len(ski_list)):
#         resorts_list[i] = SkiWeather(ski_list[i])
    
#     print("\nresorts_list: ", str(resorts_list))
#     print("\nnames[0] =", resorts_list[0].name())

#     print("\ndates", resorts_list[0].date())
#     print("totalSnowfall_cm[0] =", resorts_list[0].totalSnowfall_cm())
#     print("chanceofsnow()[0] =", resorts_list[0].chanceofsnow())

#     print("\ntop_max =", resorts_list[0].top_max())
#     print("top_min =", resorts_list[0].top_min())
#     print("\nmid_max =", resorts_list[0].mid_max())
#     print("mid_min =", resorts_list[0].mid_min())
#     print("\nbottom_max =", resorts_list[0].bottom_max())
#     print("bottom_min =", resorts_list[0].bottom_min())
 
#     print(resorts_list[0].chanceoffog())
#     print(resorts_list[0].chanceofthunder())
#     print(resorts_list[0].chanceofwindy())
#     print(resorts_list[0].snowfall_cm())
#     print(resorts_list[0].visibility())
#     print(resorts_list[0].chanceofrain())
#     print(resorts_list[0].whether())

#     print("\nOk!")

