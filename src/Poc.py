import requests
from bs4 import BeautifulSoup
import urllib.parse

url = "https://en.wikipedia.org/wiki/United_States_person"
url01 = "https://en.wikipedia.org/wiki/Launch_Vehicle_Digital_Computer"
def main(url):
    count = 0
    web = []
    while True:
     
        response = requests.get(url)
        
        if response.status_code == 200:
            count+=1
            parsedurl = urllib.parse.urlparse(url)
            urlbase = "https://"+(parsedurl.netloc)
            content = BeautifulSoup(response.text, 'html.parser')
            #(content.prettify())
            
            list_of_A = content.findAll('a', href=True)
            
            for each in list_of_A:
                
                newurl = each['href']
                
                if newurl[0] == '/':
                    if newurl[1] == '/':
                        newurl =  "https:"+newurl
                    else:
                        newurl = urlbase + newurl
                    ts = "&"
                    if("&" in newurl):
                        ts = ""
                        indx = newurl.find("&")
                        newurl = newurl[:indx]
                    web.append(newurl)
                
                elif("http" in newurl and any(x in newurl for x in [".org", ".co",".in",".gov", ".com"])):
                    web.append(newurl)
                    #status = requests.get(newurl)
            
            print(count, " ",url," ", response.status_code," ",len(web))     
        if(len(web)>0):
            url = web.pop(0)
        else:
            break
             
            
def test01(url):
    count=0
    response = requests.get(url)
   
    web = []
    if response.status_code == 200:
        parsedurl = urllib.parse.urlparse(url)
        urlbase = "https://"+(parsedurl.netloc)
        content = BeautifulSoup(response.text, 'html.parser')
        #(content.prettify())
        list_of_A = content.findAll('a', href=True)
        #print(list_of_A)
        for each in list_of_A:
            
            newurl = each['href']
            if len(newurl)>2 and newurl[0] == '/':
                if newurl[1] == '/':
                    newurl =  "https:"+newurl
                else:
                    newurl = urlbase + newurl
                count+=1
                web.append(newurl)
                status = requests.get(newurl)
                print(count, " ",newurl," ", status.status_code)


#test01("https://www.ibm.com/ibm/history/exhibits/space/space_saturn.html")
##main code
#main("https://www.ibm.com/ibm/history/exhibits/space/space_saturn.html")
main(url01)