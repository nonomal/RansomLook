import os
from bs4 import BeautifulSoup
from typing import Dict, List

def main() -> List[Dict[str, str]] :
    list_div=[]

    for filename in os.listdir('source'):
        try:
            if filename.startswith(__name__.split('.')[-1]+'-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                divs_name=soup.find_all('article')
                for div in divs_name:
                    title = div.find('h1').text.strip()
                    try:
                        description = div.find('div', {"id":"tags"}).text.strip()
                    except:
                        description = ''
                        pass
                    link = div.find('a')['href']
                    list_div.append({"title" : title, "description" : description, 'link': link, 'slug': filename})
                divs_name=soup.find_all('div')
                for div in divs_name:
                    try: 
                        try:
                            title = div.find('h3').text.strip()
                        except:
                            title = div.find('h2').text.strip()
                        try:
                            description=""
                            descs = div.find_all('p')
                            for desc in descs:
                                description +=desc.text.strip()+' '
                        except:
                            description = ''
                            pass
                        list_div.append({"title" : title, "description" : description})
                    except:
                        pass
                file.close()
        except:
            print("Failed during : " + filename)
            pass
    print(list_div)
    return list_div
