import json
import urllib.request
from API_get_data import *
from datetime import datetime, timedelta
from arrays import Array
from SkiWeather import *


def main():
    """main function in program
    Return results."""
    country = str(input("\nPlease, enter a country, where you want to ski: "))
    date = str(input("Please, input a data in format yyyy-MM-dd: "))
    if get_all_data(country, date) == "!":
        return 
    get_all_data(country, date)
    all_data_end = convert_in()  # list with SkiWeather items
    
    print("\nIn {0}'s ski resorts during {1} the next weather is predicted:\n".format(country, date))
    
    for res in all_data_end:
        if res.name() != None:
            if res.whether() == [False] * 3:
                print("\tIn {0}: the weather will not be suitable for skiing during all day.".format(res.name()))
            elif res.whether() == [True] * 3:
                print("\tIn {0}: the weather will be suitable for skiing during all day.".format(res.name()))
            else:
                print("\tIn {0}:".format(res.name()))
                if res.whether()[0] == True:
                    print("\t\tin the morning the weather will be suitable for skiing;")
                if res.whether()[0] == False:
                    print("\t\tin the morning the weather will not be suitable for skiing;")
                if res.whether()[1] == True:
                    print("\t\tin the afternoon the weather will be suitable for skiing;")
                if res.whether()[1] == False:
                    print("\t\tin the afternoon the weather will not be suitable for skiing;")
                if res.whether()[2] == True:
                    print("\t\tin the eveningg the weather will be suitable for skiing.")
                if res.whether()[2] == False:
                    print("\t\tin the evening the weather will not be suitable for skiing.")
            
    return "\n                                      Have a good rest!!!\n"


def get_all_data(country, date):
    '''(string, string) -> Nonetype
    Get and write to file weather data.'''
    ch = check_date(date)
    if not ch or ch == None:
        print("\nYou entered incongruous date\n")
        return "!"
    if ch:
        key = "f83b6a4b839e4660b8691519190605"
        form = "json"
        rsrts = get_resorts_data(country)
        lst = []
        for rsrt in rsrts:
            URL = form_url(key, rsrt, form, date) 
            # print(URL)
            dict_key = rsrt
            value = get_data(URL)
            lst.append(dict_data(dict_key, value))
        another_key = "resorts"
        write_data(another_key, lst)
    # print("Ok")


def check_date(date):
    """(string) -> bool
    Check if a date is in requisite boundaries."""
    try:
        d_max = str(datetime.today() + timedelta(days=5))
        d_max = d_max[:10]
        date_list = date.strip().split("-")[-1]
        d_max = d_max.strip().split("-")
        for i in range(3):
            if int(date_list[i]) > int(d_max[i]):
                return False
        return True
    except Exception as r:
        # print(Exception)
        return None


def convert_in():
    """(json) -> Array(SkiWeather)
    Сonvert data from a file to instances of the class."""
    
    f = open('data.json', encoding = 'utf-8')
    all_data = json.load(f)

    ski_list = list(key for key in all_data['resorts'])
    resorts_list = Array(len(ski_list))
    
    for i in range(len(ski_list)):
        resorts_list[i] = SkiWeather(ski_list[i])

    return resorts_list


print(main())