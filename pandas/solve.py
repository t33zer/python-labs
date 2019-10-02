import requests
import pandas as pd

json_city = requests.get("https://www.metaweather.com/api/location/search/?query=Tokyo").json()
ident = json_city[0]["woeid"]

temps = []
for i in range(26, 31):
    index = pd.DataFrame(requests.get("https://www.metaweather.com/api/location/" + str(ident) + "/2019/9/" + str(i)).json())
    maxi = 0
    ind = -1
    for idx in range(len(index.predictability)):
        if index.predictability[idx] > maxi:
            maxi = index.predictability[idx]
            ind = idx
    print("date: {0} - predictability: {1} - temp: {2}".format(index["applicable_date"][0], maxi, index["min_temp"][ind]))
    temps.append(index["min_temp"][ind])

avg_min_temp = sum(temps) / 5
print("[+]Average temp in range of 26-30 sept is {}".format(avg_min_temp))
