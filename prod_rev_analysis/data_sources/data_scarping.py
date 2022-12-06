# imports
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time


# variable declaration
customer_reviews = {}



def get_data_yelp(url, pages = 2):

    # url = "https://www.yelp.co.uk/biz/dishoom-london"

    print("📝Scraping started")
    for i in range(0,pages*10,10):
        page = url + f"?start={i}"
        print(f"Scraping yelp: {page}")
        response = requests.get(page)
        time.sleep(2)
        soup = BeautifulSoup(response.content, "html.parser")
        reviews = soup.find_all("div", class_ = "review__09f24__oHr9V")

        for review in reviews:
            text = review.find("p", class_="comment__09f24__gu0rG").find("span", class_="raw__09f24__T4Ezm").get_text()
            score = int(review.find("div", class_="five-stars__09f24__mBKym five-stars--regular__09f24__DgBNj display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY")["aria-label"].replace("star rating", ""))
            customer_reviews[text] = score

    print("📝Scraping from yelp completed. Converting to a dataframe.")
    df_reviews = pd.DataFrame(customer_reviews.items(),columns=['text', 'score'])
    review_count = df_reviews.shape[0]
    average_score = df_reviews.score.mean()
    return df_reviews, review_count, average_score

def hello_world():
    return "hello world. This is me arun"


def get_data_trustpilot(url, pages = 1):
    print("📝Scraping from trustpilot started")
    for i in range(1, int(pages) + 1):
        page = url + f"?page={i}"
        response = requests.get(page)
        time.sleep(2)
        soup = BeautifulSoup(response.content, "html.parser")
        reviews = soup.find_all("section", class_ = "styles_reviewContentwrapper__zH_9M")
        for review in reviews:
            text = review.find("p", class_="typography_body-l__KUYFJ").get_text()
            review_rating = int(review.find("div", class_="star-rating_starRating__4rrcf star-rating_medium__iN6Ty").find("img")["alt"][6])
            customer_reviews[text] = review_rating
    print("📝Scraping from turstpilot completed. Converting to a dataframe.")
    df_reviews = pd.DataFrame(customer_reviews.items(),columns=['text', 'score'])
    review_count = df_reviews.shape[0]
    average_score = df_reviews.score.mean()
    return df_reviews, review_count, average_score

# output = get_data_trustpilot("https://uk.trustpilot.com/review/www.hsbc.co.uk")
# print(output)

# print("DF")
# print(output[0])
# print("review count")

# print(output[1])
# print("average score")

# print(output[2])
