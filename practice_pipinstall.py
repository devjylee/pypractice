# pip3 install
# pip3 install --upgrade
# pip3 uninstall 

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())