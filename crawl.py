import requests
import time
import subprocess
import os
from bs4 import BeautifulSoup


pages=[]
titles=[]
prices=[]
rating=[]

entry= {'titles' : titles, 'prices' : prices, 'ratings' : rating, 'pages' : pages}
count_page=1

option=input('''Enter the options\n 1. Enter the name of a website to extract all links\n 2. Extracting data like price, Titles, Rating "from books.toscrape.com"\n 3. List the subdomains of a website\n 4. List all directories of a website\n''')



def subdomains():
    url= input('enter the website name-->')
    cmd='python sublist3r.py -d {} -o list.txt'.format(url)
    subprocess.call(cmd)
    os.system("list.txt")


while True:
    if option=='3':
        subdomains()

    elif option=='4':
        url=input("enter the website name-->")

        with open("directories.txt", 'r') as file:
                print("****list of Directories***\n")
                for line in file:
                    line = line.strip()
                    test_url = url + '/' + line
                    response = requests.get("http://"+ test_url)
                    if response:
                        print(test_url)

    elif option=='2':
        

        for i in range(1, count_page+1):         # to extract all the pages
            url = 'http://books.toscrape.com/catalogue/page-'+ str(i) +'.html'
            pages.append(url)
    ##print(pages)

        for item in pages:
            page = requests.get(item)
            soup = BeautifulSoup(page.text, 'html.parser')
        #(soup.prettify())

        for i in soup.find_all('h3'):
            ttl = i.getText()
            titles.append(ttl)
        
        for i in soup.find_all('p' , class_='price_color'):
            rates = i.getText()
            prices.append(rates)
        
        for i in soup.find_all('p' , class_='star-rating'):
            for k,v in i.attrs.items():
                #print(k,v)
                star=v[1]
                rating.append(star)
        
        div = soup.find_all('div', class_='image_container')
        for thumb in div:
            tgs= thumb.find_all('img', class_='thumbnail')
            #url= 'http://books.toscrape.com/' + str(tgs['src'])
            #print(url)
        print('**********Title of the books********\n')    
        print(titles)
        print('**********Prices of the books********\n')
        print(prices)
        print('**********Rating of the books********\n')
        print(rating)
        
    elif option=='1':
        url = input('enter the website name like example.com -->')
        page = requests.get('http://'+ url)    
        data = page.text
        soup = BeautifulSoup(data)
        for link in soup.find_all('a'):
            time.sleep(1)
            print(link.get('href'))

    value=input('Do you want to continue y/n--->')

    if value=='y':
        option=input('''Enter the options\n 1. Enter the name of a website to extract all links\n 2. Extracting data like price, Titles, Rating "from books.toscrape.com"\n 3. List the subdomains of a website\n 4. List all directories of a website\n''')

        continue
    else:
        break
        

