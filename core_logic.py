import requests


def core(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
    return requests.get(url)
