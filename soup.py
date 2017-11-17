from bs4 import BeautifulSoup
import urllib

# file = open("soup.","w")


r = urllib.urlopen("http://www.dictionary.com/browse/sheep?s=t")
soup = BeautifulSoup(r, "html5lib")
definitions = soup.find_all("div", class_="def-set")
# definitionsin = soup.find_all()
for element in definitions:
    sdef = element.find(class_="def-content")
    print sdef
# print sdef
# file.write(str(soup))