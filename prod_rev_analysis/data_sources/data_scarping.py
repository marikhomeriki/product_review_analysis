# imports
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time


# variable declaration
customer_review = {}



def get_data_yelp(url, pages = 2):

    # url = "https://www.yelp.co.uk/biz/dishoom-london"

    print("📝Scrapping started")
    for i in range(0,pages*10,10):
        page = url + f"?start={i}"
        print(f"Scrapping {page}")
        response = requests.get(page)
        time.sleep(3)
        soup = BeautifulSoup(response.content, "html.parser")
        reviews = soup.find_all("div", class_ = "review__09f24__oHr9V")
        for j,review in enumerate(reviews):
            text = review.find("p", class_="comment__09f24__gu0rG").find("span", class_="raw__09f24__T4Ezm").get_text()
            review_rating = review.find("div", class_="five-stars__09f24__mBKym five-stars--regular__09f24__DgBNj display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY")["aria-label"]
            customer_review[f"review_{j+i}"] = text
            customer_review[f"score_{j+i}"] = review_rating
    print("📝Scrapping completed. Converting to a dataframe.")

    df_reviews = pd.DataFrame([(customer_review[f"review_{i}"],float(customer_review[f"score_{i}"].replace("star rating", "")))for i in range(int(len(customer_review)/2))])
    df_reviews.columns = ["Review", "Score"]
    # df_reviews["Score"] = df_reviews.Score.str.replace("star rating", "")
    print(df_reviews.head())
    print(df_reviews.shape)
    review_count = df_reviews.shape[0]
    average_score = df_reviews.Score.mean()
    print(f"Review count: {review_count}")
    print(f"Average score: {average_score}")

    print("📝Creating a CSV.")
    df_reviews.to_csv('../yelp_reviews.csv')

    return {"total_reviews" : review_count, "average_score" : average_score}

def hello_world():
    return "hello world. This is me arun"
