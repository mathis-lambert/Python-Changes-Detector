# import urllib library
import time
import webbrowser
from urllib.request import urlopen
# import json
import json
# store the URL in url as 
# parameter for urlopen
browserName = input("Enter the browser name: ")
browserPath = input("Enter the browser path: ")

webbrowser.register(browserName, 
                    None, 
                    webbrowser.BackgroundBrowser(browserPath))

print("bienvenue dans le programme de recuperation de l'URL du fichier json, concu par Lextan, Pour les JDL")
url = "https://proxima.lextan.co/teams/url.json"	
# store the response of URL
# every five seconds open url
def openUrl(url):
    url = url
    response = urlopen(url)

    # storing the JSON response 
    # from url 
    return json.loads(response.read())

list_of_known_urls = []
webbrowser.get(browserName).open(openUrl(url)["url"])



while True :
    time.sleep(1)
    list_of_known_urls.append(openUrl(url)['url'])
    list_lenght = len(list_of_known_urls)
    
    
    if list_lenght > 2:
        
        list_of_known_urls.pop(1)
        list_lenght = len(list_of_known_urls)
        
        if list_of_known_urls[list_lenght-2] != list_of_known_urls[list_lenght-1]:
            print("URL mis a jour", list_of_known_urls)
            webbrowser.get(browserName).open_new_tab(list_of_known_urls[list_lenght-1])
            list_of_known_urls[0] = list_of_known_urls[list_lenght-1]   
            