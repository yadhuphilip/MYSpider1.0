import requests
from bs4 import BeautifulSoup


def urlValidator(url):

    if any(word in url for word in URLVALIDSTRINGS):
        return True
    return False   


##CONSTANTS
ENTRY_URL = "https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3"
URLVALIDSTRINGS = ["http", "https", ".com", ".in", ".org", ".co", ".gov"]


######
world = []
count = 0
######

while ENTRY_URL and count<=1000:
    
    response = requests.get(ENTRY_URL)
    if response.status_code == 200:

        content = BeautifulSoup(response.text, 'html.parser')
        #(content.prettify())
        list_of_A = content.findAll('a', href=True)

        for each in list_of_A:
            # print(each['href'] ,"\n")
            if( urlValidator( each['href'])):
                #print(each['href'], urlValidator( each['href'] ),"\n")
                world.append(each['href']) 
                count+=1
    if world is not None:
        ENTRY_URL = world.pop(0)

print(count)


 