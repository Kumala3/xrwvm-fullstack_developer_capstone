import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5050/"
)


def get_request(endpoint: str, **kwargs):
    params = ""
    if kwargs:
        params = "&".join([f"{key}={value}" for key, value in kwargs.items()])

    request_url = f"{backend_url}{endpoint}?{params}"
    # if params:
    #     request_url = request_url.rstrip("?")

    print(f"GET request from {request_url} ")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response
    except Exception:
        print("Network exception occurred")  # If any error occurs


def analyze_review_sentiments(text: str):
    request_url = f"{sentiment_analyzer_url}analyze/{text}"

    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# def post_review(data_dict):
# Add code for posting review
