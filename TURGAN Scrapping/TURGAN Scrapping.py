import email
import urllib
import urllib.request as u
import re
from bs4 import BeautifulSoup
import csv
header = ['Name','Language', 'Telephone No.','Mobile No.','Email']
url="https://tourguidenepal.org.np/members"
page= u.urlopen(url)
soup=BeautifulSoup(page,"html.parser")
containers=soup.findAll("div",{"class":"member-details"})
filename = "Details.csv"
with open(filename, 'w+') as f:
    writer = csv.writer(f)
    writer.writerow(i for i in header)
    for container in containers:
        name = container.li
        language = name.findNextSibling()
        telephone = language.findNextSibling()
        mobile_no = telephone.findNextSibling()
        email_add = mobile_no.findNextSibling()
        print(name.text)
        print(language.text)
        print(telephone.text)
        print(mobile_no.text)
        print(email_add.text)
        row=[name.text,language.text,telephone.text,mobile_no.text,email_add.text]
        writer.writerow(row)