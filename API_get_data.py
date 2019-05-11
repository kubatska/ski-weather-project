import json
import urllib.request


def get_resorts_data(country):
    """
    (None) -> list
    Read a file and return a list of resorts.
    """
    with open("data_resorts.txt", encoding='utf-8', errors='ignore') as f:
        try:
            lst_with_resorts = []
            for line in f:
                line = line.strip().split(',')
                if line[0] == country:
                    resorts = line[1][1:]
                    for i in resorts:
                        if i == "-":
                            resorts = resorts.replace("-", "+")
                        if not i.isalpha():
                            resorts = resorts.replace("   ", " ")
                            resorts = resorts.replace("  ", " ")
                            resorts = resorts.replace(" ", "+")
                            resorts = resorts.replace("++", "+")
                    lst_with_resorts.append(resorts)
        except:
            print("Error")
        return lst_with_resorts


def form_url(key, q, form, date):
    """
    (list) -> string
    Return a URL string.
    -------------------------
    parameters:
    key - yout API key;
    q - City or town name, or IP address, UK or Canada Postal Code or US Zipcode, Latitude and longitude;
    format - JSON, HML;
    date - in the yyyy-MM-dd format, if this parameter absent it is considerd today;
    """
    return """http://api.worldweatheronline.com/premium/v1/ski.ashx?key={0}&q={1}&format={2}&date={3}&includelocation=yes&tp=6&showlocaltime=yes""".format(key, q, form, date)


def get_data(URL):
    """
    (string) - dict
    Return JSON file
    """
    data = urllib.request.urlopen(URL).read().decode()
    file = json.loads(data)
    return file


def dict_data(dict_key, value):
    """
    (str, dict) -> dict
    Return a dict.
    """
    dict_a = dict()
    dict_a[dict_key] = value
    return dict_a


def write_data(another_key, lst):
    """
    (str, list) -> Nonetype
    Write a dict to file.
    """
    dict_a = dict()
    dict_a[another_key] = lst
    with open('data.json', 'w', encoding = 'utf-8') as f:
        json.dump(dict_a, f, ensure_ascii=False)


# if __name__ == "__main__":
#     country = str(input("Please, enter a country: "))
#     # date = str(input("Please, input a data in format yyyy-MM-dd: "))
#     # date = "2019-03-10"
#     num_of_days = "5"
#     key = "f83b6a4b839e4660b8691519190605"
#     form = "json"
#     rsrts = get_resorts_data(country)
#     lst = []
#     for rsrt in rsrts:
#         # URL = form_url(key, rsrt, form, date)
#         URL = form_url(key, rsrt, form, num_of_days)
#         print(URL)
#         dict_key = rsrt
#         value = get_data(URL)
#         a = dict_data(dict_key, value)
#         lst.append(a)
#     another_key = "resorts"
#     write_data(another_key, lst)
#     print("Ok")




