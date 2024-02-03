import wget
# from termcolor import cprint
def main(urls, l1, l2):
    file = open(urls, 'r')
    urls = file.readlines()
    if l1 != 0:
        l1 -=1
    if l2 == 0:
        l2 = len(urls)
    
    print("\nDownloading ", l2 - l1, " files ...\n--------------------------", end="")

    for i, url in enumerate(urls[l1:l2]):
        fname = url.split("filename=")[1][:-1]
        print(f"\nReaching file[{i+1}]: ", end="")
        print(fname)
        filename = wget.download(url.replace( " ", "%20"), out= fname)

if __name__ == "__main__":

    path = input("Filename:")    
    l1 = int(input("First line to start with:"))
    l2 = int(input("Last line to download:"))
    
    
    if path == '':
        path = 'jpg_urls.txt'
    

    main(path, l1, l2)