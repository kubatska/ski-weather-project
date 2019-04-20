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
        return [wea["totalSnowfall_cm"] for wea in weather]
           
           
    def chanceofsnow(self):
        """(SkiWeather) -> list 
        Return chance of snow in a day"""
        weather = self.get_weather()
        if weather is None:
            return None
        return [wea["chanceofsnow"] for wea in weather]


    def hourly(self):
        """(SkiWeather) -> list 
        Return information about the weather forecast for the hour."""
        weather = self.get_weather()
        if weather is None:
            return None
        return [wea["hourly"] for wea in weather]


    def date(self):
        """(SkiWeather) -> list 
        Return local forecast date"""
        weather = self.get_weather()
        if weather is None:
            return None
        return [wea["date"] for wea in weather]


    def bottom_min(self):
        """(SkiWeather) -> list"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["bottom"][0]
            res.append(wea_['maxtempC'])
        return res
        
    def bottom_max(self):
        """(SkiWeather) -> list"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["bottom"][0]
            res.append(wea_['mintempC'])
        return res

    def mid_min(self):
        """(SkiWeather) -> list"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["mid"][0]
            res.append(wea_['maxtempC'])
        return res
        
    def mid_max(self):
        """(SkiWeather) -> list"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["mid"][0]
            res.append(wea_['mintempC'])
        return res


    def top_min(self):
        """(SkiWeather) -> list"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["top"][0]
            res.append(wea_['maxtempC'])
        return res
        
    def top_max(self):
        """(SkiWeather) -> list"""
        weather = self.get_weather()
        if weather is None:
            return None
        res = []
        for wea in weather:
            wea_ = wea["top"][0]
            res.append(wea_['mintempC'])
        return res
    
    def __str__(self):
        return str(self.name())



if __name__ == "__main__":
    f = open('data.json', encoding = 'utf-8')
    all_data = json.load(f)

    ski_list = list(key for key in all_data['resorts'])
    resorts_list = Array(len(ski_list))
    
    for i in range(len(ski_list)):
        resorts_list[i] = SkiWeather(ski_list[i])
    
    print("\nresorts_list: ", str(resorts_list))
    print("\nnames[0] =", resorts_list[0].name())

    print("\ndates", resorts_list[0].date())
    print("totalSnowfall_cm[0] =", resorts_list[0].totalSnowfall_cm())
    print("chanceofsnow()[0] =", resorts_list[0].chanceofsnow())

    print("\ntop_max =", resorts_list[0].top_max())
    print("top_min =", resorts_list[0].top_min())
    print("\nmid_max =", resorts_list[0].mid_max())
    print("mid_min =", resorts_list[0].mid_min())
    print("\nbottom_max", resorts_list[0].bottom_max())
    print("bottom_min", resorts_list[0].bottom_min())

    print("\nOk!")

