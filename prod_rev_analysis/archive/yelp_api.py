
# imports
import os
from dotenv import load_dotenv, find_dotenv
import requests

# point to .env file
env_path = find_dotenv() # automatic find

# load your api key as environment variables
load_dotenv(env_path)

yelp_api_key = os.getenv('YELP_API_KEY')

end_point = "https://api.yelp.com/v3/businesses/search"

location = input("Enter location: ")

parameters = {
    "location" : location,
}

header ={
    "Authorization": yelp_api_key
    }

response = requests.get(end_point, params=parameters, headers=header)
print(response.raise_for_status())
result = response.json()

print(result)
