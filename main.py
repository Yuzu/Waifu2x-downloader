import requests
import urllib
import os
import json

def main():

    key = getApiKey()

    files = os.listdir("in")

    for image in files:
        processImage("in/{0}".format(image), key)


def processImage(filePath: str, apiKey: str):

    try:
        r = requests.post("https://api.deepai.org/api/waifu2x",
                                files={
                                    "image": open(filePath, "rb")
                                },
                                headers = {'api-key': apiKey}
                          )

        out = r.json()
        fileName = filePath.split("/")[1]  # "in/hello.jpg" turns into "hello.jpg"

        if len(out) == 1:  # If an error occurs on DeepAI's end, it will return a 1 len json w/ an error message.
            print("An error has occurred with file {0}.".format(filePath))
            return

        urllib.request.urlretrieve(out["output_url"], "out/{0}".format(fileName))

    except Exception as e:
        print("An error has occurred! {0}".format(e))


def getApiKey():
    with open("key.json", "r") as f:
        data = json.load(f)
        return data["key"]


if __name__ == "__main__":
    main()