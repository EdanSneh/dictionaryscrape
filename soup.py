from bs4 import BeautifulSoup
import urllib

# file = open("soup.txt","w")


r = urllib.urlopen("http://www.dictionary.com/browse/machine-learning?s=t")
soup = BeautifulSoup(r, "html5lib")
soup.prettify()

definitions = soup.find_all("div", class_="def-set")

# definitionsin = soup.find_all()
for element in definitions:
    try:
    	defcontent = element.find(class_="def-content").get_text() 
    	defnum = element.find(class_="def-number").get_text()
    except Exception as e:

    	print e
    print defnum + " " + defcontent.replace("  ","").replace("\n","")
# print sdef

# file.write(str(soup))
