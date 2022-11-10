from bs4 import BeautifulSoup
import requests
from typing import *

def link_scrapper(url ,html_cmd):
    r'''
    Arguments:-
    url : webpage url in string format
    html_cmd : For scrapping the particular area in the web page , we need html command in list format eg:['nav','class' ,'ddc-paging']
    
    Return:-
    links : Scrapped links 
    keys : Values scrapped from the web pages'''

    #Requests module use to data from given url
    source=requests.get(url)

    # BeautifulSoup is used for getting HTML structure from requests response.
    soup=BeautifulSoup(source.text,'html')
    body = soup.body.findAll (html_cmd[0] ,{html_cmd[1]:html_cmd[2]})
    
    #Extracting the links present on the web page for further exploration
    medicines = {}
    links = []
    a = 0
    for tags in body:
        for t in tags.find_all('a', href=True):
            links.append(t.get('href'))
            medicines[a] = t.get_text('href')
            a += 1
            
    keys = list(medicines.values())
    return links  ,keys
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def content_scrap(links ,keys):
    r'''
    Arguments:-
    links : Webpage links which you want to scrap {format = List[strings]} 
    keys  : Values which was returned by the link_scrapper function
    
    Return:-
    It will return the scrapped content.
    '''
    names={}
    start = 0

    # Iterating through the links and extracting data
    suc = 0
    fail = 0
    failed_links = []
    for i in range(start,len(links)) :
        print (" Extracting data for -", keys[i])    
        link_url =  links[i]    
        source=requests.get(link_url)

        # BeautifulSoup is used for getting HTML structure from requests response.
        soups=BeautifulSoup(source.text,'html')
        page = pages (soups ,keys[i])
        
        # Avoiding errors
        try :
            if len(page) != 0 :
                print("Success in extracting data for - ",keys[i])
                print("Copying the data from the web........")
                names[keys[i]] = page
                print("DONE")
                print("*"*50)
                suc += 1

            else :
                print("No data was extracted for - ", keys[i])
                names[keys[i]] = None
                print("*"*50)
                fail += 1
                failed_links.append(link_url)
        except :
            
            print("No data was extracted for - ", keys[i])
            #names[keys[i]] = None
            print("*"*50)
            fail += 1
            failed_links.append(link_url)
    # Let's see the links from which the data extraction was a success/unsuccess
    print("No.of links from which data was extracted succesfully-", suc)
    print("No.of links from which data extraction was unsuccesfull-", fail)
    print("*"*20,'PROCESS COMPLETED',"*"*20)
    return names

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# function for extraction of required data by converting the contents as text and searching the required section
def pages (soups_ ,keys):
    
    #Extracting the text present in class = "contentBox"
    for tags in soups_.find_all("p",{"class": "drug-subtitle"}):
        try:
             return  (tags.get_text())
        except UnboundLocalError: 
            return keys
    