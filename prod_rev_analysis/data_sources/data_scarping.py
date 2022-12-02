# imports
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time


# variable declaration
customer_review = {}


url = ""
def get_data_yelp(url, pages = 30):

    # url = "https://www.yelp.co.uk/biz/dishoom-london"

    page_numbers = int(input("Pages of reviews to include: "))

    print("📝Scrapping started")
    for i in range(0,page_numbers*10,10):
        page = url + f"?start={i}"
        response = requests.get(page)
        time.sleep(1)
        soup = BeautifulSoup(response.content, "html.parser")
        reviews = soup.find_all("div", class_ = "review__09f24__oHr9V")
        for j,review in enumerate(reviews):
            text = review.find("p", class_="comment__09f24__gu0rG").find("span", \
                class_="raw__09f24__T4Ezm").get_text()
            review_rating = review.find("div", class_="five-stars__09f24__mBKym \
                five-stars--regular__09f24__DgBNj display--inline-block__09f24__fEDiJ \
                    border-color--default__09f24__NPAKY")["aria-label"]
            customer_review[f"review_{j+i}"] = text
            customer_review[f"score_{j+i}"] = review_rating

    print("✅ Scrapping done")

    df_reviews = pd.DataFrame([(customer_review[f"review_{i}"],customer_review[f"score_{i}"])for i in range(int(len(customer_review)/2))])
    df_reviews.columns = ["Review", "Score"]
    df_reviews["Score"] = df_reviews.Score.str.replace("star rating", "")
    df_reviews

    print(df_reviews.head())
    print(df_reviews.shape())

    review_count = df_reviews.shape[0]

    df_reviews.to_csv('/Users/ankurkaushal/code/project_review_scarpe/reviews.csv')
    print("✅ .csv created")

    return review_count
