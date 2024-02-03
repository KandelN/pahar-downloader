from bs4 import BeautifulSoup
import requests

# generate list of main webpages:
parent = 'https://pahar.in/nepal-topo-maps/'
mainurls = [ parent + '?cp=' + str(i) for i in range(1,9)]
print(mainurls)

# generate list of sub webpages and store in text file:
print("\n\n======================\n Generating sub webpages links and writing in the text file.")
f1 = open("sub_pages.txt", "w+")
sub_urls = []
def write_subpages(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # soup = BeautifulSoup(open("C:\\Users\\Nelson\\Downloads\\pahar_raw.html", encoding="utf8"), "html.parser")

    mydivs = soup.find_all("div", {"class": "col-lg-12 col-md-6 col-12"})

    
    for mydiv in mydivs:
        link = mydiv.find('a')['href']
        f1.write(link + "\n")
        print("WRITTEN:", link)
        sub_urls.append(link)

for kids in mainurls:
    write_subpages(kids)
f1.close()
print("Completed writing in the file sub_pages.txt")

# Alternatively read file
# f1 = open("sub_pages.txt", 'r')
# sub_urls= f1.readlines()

# generate list of jpg urls and store in text file:

print("\n\n======================\n Generating jpg urls links and writing in the text file.")
f2 = open("jpg_urls.txt", "w+")
def write_jpg_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    jpgurl = soup.find("a", {"class": "inddl btn btn-primary btn-sm"}).get("href")
    f2.write(jpgurl + "\n")
    print("WRITTEN JPG URL", jpgurl)

for url in sub_urls:
    write_jpg_url(url)

f2.close()
print("Completed writing in the file jpg_urls.txt")
