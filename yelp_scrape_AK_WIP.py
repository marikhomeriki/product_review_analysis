import requests
from bs4 import BeautifulSoup


url = input("Enter url: ") #"https://www.yelp.co.uk/biz/dishoom-london"

for i in range(0,222,10):
    page = ""
    page = url + f"?start={i}"
    print(page)

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

reviews = soup.find_all("div", class_ = "review__09f24__oHr9V")

customer_review = {}

for i,review in enumerate(reviews):
     text = review.find("p", class_="comment__09f24__gu0rG").find("span", class_\
         ="raw__09f24__T4Ezm").get_text()
    #  score = review.\
    #      find("div", class_ = "display--inline-block__09f24__fEDiJ")\
    #          .find("span", class_="display--inline__09f24__c6N_k")
     customer_review[f"review_{i}"] = text,
     customer_review[f"score_{i}"] = 1000

# soup.find("ul", class_ = "undefined")
print(customer_review)
