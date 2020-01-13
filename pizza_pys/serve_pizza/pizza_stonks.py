
# Problem what the hell is the true value of pizza today.
# Do you want to do those calculations every single time.
# No! Let's create a service that do.
#
# Pizza Stonks! ..V0.1.69
#
# Author: Jordan Dysart
# Date  : December 18, 2019
# 
# Purpose: Gather Pizza values by webscraping the local pizza joints

import requests

from bs4 import BeautifulSoup

PROTO = "https://"
DOMAIN = "bostonpizza.com"
path = "/en/menu/pizza.html"



headers = {
    'authority': 'bostonpizza.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://bostonpizza.com/en/menu/pizza.html',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=d3939549a779ef015fb1b24ebf5255b541576716933; _gcl_au=1.1.104489770.1576716935; AMCVS_C0F6470957CF08467F000101%40AdobeOrg=1; s_ecid=MCMID%7C06701214401335144862475121455571620587; _ga=GA1.2.1534886718.1576716935; _gid=GA1.2.348872930.1576716935; s_cc=true; _fbp=fb.1.1576716936604.540194440; AMCV_C0F6470957CF08467F000101%40AdobeOrg=-894706358%7CMCIDTS%7C18250%7CMCMID%7C06701214401335144862475121455571620587%7CMCOPTOUT-1576734461s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.3.0; menuStore=cityplace-mall; userLocationAccepted=true; geoipResponse=%7B%22coords%22%3A%7B%22latitude%22%3A%2249.890444018724892%22%2C%22longitude%22%3A%22-97.14267965920817%22%7D%7D; storeDetails=%7B%22restaurantId%22%3A%22c6fb2192-b736-4be6-8fc8-7d770398f14e%22%2C%22restaurantName%22%3A%22Cityplace%20Mall%22%2C%22restaurantJcrName%22%3A%22cityplace-mall%22%2C%22restaurantRedirectionPath%22%3A%22/content/bostonpizza/en/locations/cityplace-mall%22%2C%22menuRedirectionPath%22%3A%22/content/bostonpizza/en/menu%22%2C%22menuGroupName%22%3A%22M1%22%2C%22latitude%22%3A%2249.890444018724892%22%2C%22longitude%22%3A%22-97.14267965920817%22%2C%22deliveryPhoneNumber%22%3A%2212049254109%22%2C%22restaurantPhoneNumber%22%3A%220012049254109%22%2C%22storeId%22%3A%22319%22%2C%22cookieType%22%3A%22identifiedStore%22%7D; gpv_pn=bp%3Achristmas%20pizza; s_sq=%5B%5BB%5D%5D'}



def main():
    print("hello world, give me pizza!")

    # Get Boston pizza menu
    URL = "https://bostonpizza.com/en/menu/pizza.html"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    pizza_class = "concierge-menu-cta"
    pizza_links = getPizzaLinksFromMenu(soup, pizza_class)
    for pizza_link in pizza_links:
        print(pizza_link)

    # Let's go get a pizza price from the first link
    path = pizza_links[0]
    request_url = PROTO + DOMAIN + path
    pizza = requests.get(request_url, headers=headers)
    pizza_soup = BeautifulSoup(pizza.content, 'html.parser')

    # Get pizza deets
    print('getting pizza deets')
    pizza_class = "pizzaSizeSelection"
    pizza_deets = getPizzaDeets(pizza_soup, pizza_class)

    print(pizza_deets)
    print('end of doc')




def getPizzaLinksFromMenu(soup, pizza_class):
    '''
    takes a pizza site url, class and finds all pizza links.
    returns a list of pizza links
    Still subject to change.
    '''
    results = []
    for pizza_link in soup.find_all('a', class_=pizza_class):
        if "pizza/" in pizza_link.get('href'):
            results.append(pizza_link.get('href'))
    return results

def getPizzaDeets(soup, pizza_class):
    '''
    takes a pizza site url, class and finds all pizza links.
    returns a list of pizza links
    Still subject to change.
    '''
    results = []
    for pizza_link in soup.find_all('input', class_=pizza_class):
        results.append(pizza_link.attrs)
        print(pizza_link.attrs)
    return results

if __name__ == '__main__':
    main()
