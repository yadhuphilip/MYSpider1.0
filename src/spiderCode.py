import requests
from bs4 import BeautifulSoup


def urlValidator(url):
    #print("debug")
    if any(word in url for word in URLVALIDSTRINGS):
        return True
    return False   

def prepareUrlForFile(cnt, newUrl):

    preparedData = str(cnt)+ " " + newUrl + " \n"
    return preparedData

##CONSTANTS
LIMIT = 4000
ENTRY_URL = "https://en.wikipedia.org/wiki/Launch_Vehicle_Digital_Computer" 
#"https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3"
URLVALIDSTRINGS = ["http", "https", ".com", ".in", ".org", ".co", ".gov"]
FILE_NAME = "urlDB.txt"
UNIQUE_SET = set()
UNIQUENESS = 1


######
world = []
count = 1
######

fPtr = open(FILE_NAME,'w')
while ENTRY_URL and count <= LIMIT:
    flag = 1

    
    response = requests.get(ENTRY_URL)
    if response.status_code == 200:
        content = BeautifulSoup(response.text, 'html.parser')
        #(content.prettify())
        list_of_A = content.findAll('a', href=True)

        for each in list_of_A:
            newUrl = each['href']
            if(count >0 and count % UNIQUENESS==0 ):
                UNIQUE_SET.clear()
            if( newUrl in UNIQUE_SET):
                flag = 0
            else:
                UNIQUE_SET.add(newUrl)

            if( urlValidator(newUrl) and flag):

                world.append(newUrl) 
                preparedStr = prepareUrlForFile(count, newUrl)
                count+=1
                if(count>0 and count%15==0):
                    print("###-- " , count , "--###")
                fPtr.write(preparedStr)
    if len(world) > 0:
        ENTRY_URL = world.pop(0)
    else:
        break
        
fPtr.close()
print(count)


 