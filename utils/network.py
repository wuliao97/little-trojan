import os
import re
import sys
import uuid
import requests


def getNetwork():
    def geolocation(ip: str):
        url = "http://ip-api.com/json/" + ip
        response = requests.get(url)
        data = response.json()

        return (data["country"], data["regionName"], data["city"], data["zip"], data["as"])

    ip = requests.get("https://api.ipify.org").text
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    country, region, city, zip_, as_ = geolocation(ip)
    
    return {
        "IP Address": ip,
        "MAC Address":mac,
        "Country":country,
        "Region":region,
        "City":city,
        "zip":zip_,
        "ISP":as_
    }