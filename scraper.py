from bs4 import BeautifulSoup
import requests

def check_use(drug_name):
    output = {}
    page = f'https://pharmeasy.in/search/all?name={drug_name}'

    source=requests.get(page)
    soup=BeautifulSoup(source.text,'html')
    body = soup.body.findAll ('a' ,{'class':'ProductCard_medicineUnitWrapper__238qP ProductCard_defaultWrapper__3htqi'})

    source = requests.get('https://pharmeasy.in/'+str(body[0]).split('"')[3])
    soup=BeautifulSoup(source.text,'html')
    
    body = soup.body.findAll ('td' ,{'class':'DescriptionTable_field__1aXTD'})
    body1 = soup.body.findAll ('td' ,{'class':'DescriptionTable_value__1afug'})
    body2 = soup.body.findAll ('div' ,{'class':'Section_section__QOSbs'})
    if len(body2) ==0: return "Sorry we couldn\'t find the use cases "
    for i in zip(body ,body1): output[str((i[0])).split('>')[1].split('<')[0]] = str((i[1])).split('>')[1].split('<')[0]
   
    output['role'] = output[''] 
    del(output[''] )

    return output