'''Go to careerguide.com (or any other website of your choice where you can find job types)
. Scrape Job types from there. Subcategories divided by Categories.For eg:(Education->Tutor,
 Design and Art->Architect)
URL : https://www.careerguide.com/career-options'''



from unicodedata import category
from bs4 import BeautifulSoup
import requests
url="https://www.careerguide.com/career-options"

response= requests.get(url)
htmlcontent=response.content

soup = BeautifulSoup(htmlcontent,'html.parser')
category=soup.find('div',attrs={'class':'col-md-4'})

for sub_category in category: 
    print(sub_category.text)  # catergory and sub_category print this line
    print("\n") 
