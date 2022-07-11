import requests
from datetime import datetime
import hashlib
from dotenv import load_dotenv
import os


def sign_requests(timestamp, public_key, private_key):
    """Generates a string to sign requests for the marvel api

    outputs
        signature: request signature to append to api call
    """

    hash = hashlib.md5(f"{timestamp}{private_key}{public_key}".encode("utf-8"))
    signature = hash.hexdigest()

    return signature


def call_marvel_api(request_string):
    """Call marvel api and return response

    outputs:
        response.json: json of the response request"""

    response = requests.get(request_str)

    if response.status_code == 200:
        return response.json()

    raise Exception("An error occured with the API. Please check the request string and try again")


def character_description(response):
    """Return response description

    outputs
        description: description of character"""

    if not response["data"]["results"]:
        raise Exception("Character not found, please try again.")

    if not response["data"]["results"][0]["description"]:
        raise Exception("No description found for character.")

    description = response["data"]["results"][0]["description"]

    return description


if __name__ == "__main__":

    load_dotenv()

    public_key = os.getenv("public_key")
    private_key = os.getenv("private_key")

    now = datetime.now()
    now_str = now.strftime("%d%m%Y%H%M%S")

    signature = sign_requests(now_str, public_key, private_key)

    base_url = "https://gateway.marvel.com/v1/public/"

    character = input("Pick a marvel character: ")

    character_url = "%20".join(character.split())

    request_str = f"{base_url}characters?name={character}&ts={now_str}&apikey={public_key}&hash={signature}"

    response = call_marvel_api(request_str)

    description = character_description(response)

    print(description)