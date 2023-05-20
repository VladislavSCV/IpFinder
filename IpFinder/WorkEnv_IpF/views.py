import sqlite3

import requests
from django.http import JsonResponse
from django.shortcuts import render


def searchIPfj(request, ip):
    ipshka = requests.get(url=f"http://ip-api.com/json/{ip}").json()
    return JsonResponse(ipshka)


def searchIP(request):
    ip = request.GET.get("ip-address", "127.0.0.1")
    ipshka = requests.get(url=f"http://ip-api.com/json/{ip}?fields=63700991").json()
    data = {"IP": ipshka.get("query"), "COUNTRY": ipshka.get("country"), "CC": ipshka.get("countryCode"),
            "REGION": ipshka.get("region"), "RN": ipshka.get("regionName"), "CITY": ipshka.get("city"),
            "ZIP": ipshka.get("zip"), "SHR": ipshka.get("lat"), "DOL": ipshka.get("lon"), "IPR": ipshka.get("isp"),
            "AS": ipshka.get("as"), "ASNAME": ipshka.get("asname"), "MOBILE": ipshka.get("mobile"),
            "PROXY": ipshka.get("proxy"), "TIMEZONE": ipshka.get("timezone"), "HOSTING": ipshka.get("hosting")}
    return render(request, "IpFinder.html", context=data)


# Ввод данных в db
# cursor.execute(f"""INSERT INTO user (user_name, user_password) VALUES (?, ?)""", (user_name, user_password))
def auth(request):
    user_name = request.GET.get("user_name_")
    user_password = request.GET.get("password_")
    print(user_name, user_password)
    with sqlite3.connect("DB_user_data676.db") as db:
        cursor = db.cursor()

        # Регистрация
        if user_name and user_password:
            cursor.execute(f"""INSERT INTO user (user_name, user_password) VALUES (?, ?)""", (user_name, user_password))
        db.commit()
    return render(request, "Auth.html")


def api(requests):
    return render(requests, "api.html")
