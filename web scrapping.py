'''Then you have to scrape the companies page. Details you have to scrape are :- 
Companies Description
Where is it Located'''


from unicodedata import category
from bs4 import BeautifulSoup
import requests
url="https://www.mawanasugars.com/group-profile.php"

response= requests.get(url)
htmlcontent=response.content

soup = BeautifulSoup(htmlcontent,'html.parser')

# This Logic print the company name 
print(soup.title.string) 

#This logic print the company about
company=soup.find_all('div',attrs={'class':'content-part'})
for sub_category in company: 
    print(sub_category.text) 


# This Logic print the company contact
company=soup.find_all('div',attrs={'class':'news-contouter'}) 
for sub_category in company: 
    print(sub_category.text) 
url="https://www.mawanasugars.com/contact-us.php"
response= requests.get(url)
htmlcontent=response.content
soup = BeautifulSoup(htmlcontent,'html.parser')

company=soup.find_all('div',attrs={"class":"news-contouter"}) 
for sub_category in company: 
    print(sub_category.text) 
   









