import os, requests
from bs4 import BeautifulSoup

def total_pages(code):
    link = "https://nhentai.net/g/{}/".format(code)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    todo = soup.find_all("span", class_="name")
    return todo[-1].text

def get_code_image(code):
    link = "https://nhentai.net/g/{}/1/".format(code)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    all_ = soup.find_all("img")
    code_src = all_[1].get("src")
    return code_src.split("/")[-2]

def get_extension(code, pag):
    link = "https://nhentai.net/g/{}/{}/".format(code, pag)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    all_ = soup.find_all("img")
    code_src = all_[1].get("src")
    return code_src.split(".")[-1]

def download(url, code, pag):

    os.makedirs('Downloads/'+ code, exist_ok=True)
    full_path = 'Downloads/'+ code + "/"+ pag +'.jpg'

    response = requests.get(url)
    file = open(full_path, "wb")
    file.write(response.content)
    file.close()

print("https://nhentai.net/")
code = input("code of manga: ")

code_image = get_code_image(code)
all_pages = total_pages(code)
images_link_base = "https://i.nhentai.net/galleries/{}/{}.{}"
cont = 0
for page in range(1, int(all_pages)+1):
    total = int(all_pages)+1
    percent = round(cont*100/total,1)
    print("Total pages downloaded: "+str(cont)+"/"+str(total)+" ----> "+str(percent)+"%", end="\r")
    download(images_link_base.format(code_image, str(page), get_extension(code,str(page))), code, str(page))
    cont += 1
print("Total pages downloaded: "+str(total)+"/"+str(total)+" ----> 100 %", end="\r")
input()
